import time

try:
    from deep_translator import GoogleTranslator
    from deep_translator.exceptions import TooManyRequests
except ModuleNotFoundError:
    print("Error: 'deep-translator' is not installed.")
    print("Install it with: pip install deep-translator")
    raise SystemExit(1)

languages = {
    "1": ("English", "en"),
    "2": ("Marathi", "mr"),
    "3": ("Hindi", "hi"),
    "4": ("French", "fr"),
    "5": ("German", "de"),
    "6": ("Spanish", "es"),
    "7": ("Japanese", "ja")
}


def language_translator():
    print("\n================================")
    print("       AI LANGUAGE TRANSLATOR")
    print("================================")

    while True:
        print("\nAvailable Languages:")

        for key, value in languages.items():
            print(f"{key}. {value[0]}")

        source = input("\nSelect Source Language: ").strip()
        target = input("Select Target Language: ").strip()

        if source not in languages or target not in languages:
            print("\nError: Invalid language selection!")
            continue

        if source == target:
            print("\nError: Select different languages!")
            continue

        text = input("\nEnter Text to Translate: ").strip()

        if not text:
            print("\nError: Text cannot be empty!")
            continue

        result = None
        for attempt in range(3):
            try:
                translator = GoogleTranslator(
                    source=languages[source][1],
                    target=languages[target][1]
                )
                result = translator.translate(text)
                break
            except TooManyRequests:
                print("\nGoogle translation service is busy. Retrying...")
                time.sleep(2)
            except Exception as error:
                print("\nTranslation Failed!")
                print("Reason:", error)
                print("Check your internet connection or try a different language pair.")
                result = None
                break

        if result is not None:
            print("\n========== TRANSLATION ==========")
            print("Original Text:", text)
            print("Translated Text:", result)
            print("================================")

        again = input("\nTranslate Again? (yes/no): ").strip().lower()

        if again != "yes":
            print("\nThank you for using AI Translator!")
            break


if __name__ == "__main__":
    try:
        language_translator()
    except KeyboardInterrupt:
        print("\nProgram Closed.")