using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using Microsoft.Speech.Synthesis;
using Newtonsoft.Json;

namespace SentimentRecognizer
{
    public partial class MainWindow : Window
    {
        private static readonly HttpClient client = new HttpClient();
        private static readonly SpeechSynthesizer synthesizer = new SpeechSynthesizer();

        public MainWindow()
        {
            InitializeComponent();
        }

        private async void SendButton_Click(object sender, RoutedEventArgs e)
        {
            string userInput = UserInput.Text;
            string sentiment = await SendTextToApi(userInput);

            if (sentiment == "Negatywnie")
            {
                synthesizer.Speak(sentiment);
            }

            DisplayMessage($"Użytkownik: {userInput}\nBot: {sentiment}");
            UserInput.Clear();
        }

        private async Task<string> SendTextToApi(string userInput)
        {
            if (userInput == "")
            {
                userInput = " ";
            }

            var content = new StringContent(JsonConvert.SerializeObject(new { textFromUser = userInput }), Encoding.UTF8, "application/json");

            try
            {
                var response = await client.PostAsync("http://127.0.0.1:8000/get-answer", content);
                if (response.IsSuccessStatusCode)
                {
                    var result = await response.Content.ReadAsStringAsync();
                    var jsonObject = JsonConvert.DeserializeObject<dynamic>(result);
                    var textValue = jsonObject.sentiment;

                    string positiveSentimentAnswer = "Twoja wypowiedź jest nacechowana pozytywnie :)";
                    string negativeSentimentAnswer = "Twoja wypowiedź jest nacechowana negatywnie :(";
                    string emptyMessageAnswer = "Twoja wiadomość jest pusta. Wpisz tekst, a następnie kliknij przycisk wyślij.";

                    if (textValue == "[0]")
                    {
                        return negativeSentimentAnswer;
                    }
                    else if (textValue == "[1]")
                    {
                        return positiveSentimentAnswer;
                    }
                    else
                    {
                        return emptyMessageAnswer;
                    }
                }
                else
                {
                    throw new Exception($"Błąd żądania: {response.StatusCode}");
                }
            }
            catch (Exception e)
            {
                return "Błąd: " + e.Message.ToString();
            }
        }

        private void TextBox_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Enter) 
            {
                SendButton_Click(sender, e);
            }
        }


        private void DisplayMessage(string message)
        {
            TextBlock textBlock = new TextBlock
            {
                FontSize = 14,
                Text = message,
                TextWrapping = TextWrapping.Wrap
            };
            ChatHistory.Children.Add(textBlock);
        }
    }
}