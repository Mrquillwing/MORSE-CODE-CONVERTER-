from tkinter import Tk, Label, Button, Entry, Text, END


class Root(Tk):

    def __init__(self):
        super().__init__()

        self.title("Morse Studio v1.0")
        self.geometry("100x1")

        self.history = []

        self.MORSE_CODE = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',

            '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..',
            '9': '----.',

            ' ': '/'
        }

        Label(self,
              text="MORSE STUDIO",
              font=("Arial", 12, "bold")).pack(pady=10)

        Label(self, text="Enter Text").pack()

        self.entry = Entry(self, width=50)
        self.entry.pack(pady=5)

        Button(self,
               text="Convert",
               command=self.convert).pack(pady=5)

        Button(self,
               text="Clear",
               command=self.clear).pack()

        Label(self, text="Result").pack()

        self.output = Text(self, height=9, width=1000)
        self.output.pack()

        Label(self, text="History").pack()

        self.history_box = Text(self, height=12, width=70)
        self.history_box.pack()

    def convert(self):

        text = self.entry.get().upper()

        morse = []

        for char in text:
            if char in self.MORSE_CODE:
                morse.append(self.MORSE_CODE[char])
            else:
                morse.append("?")

        result = " ".join(morse)
        pretty = result.replace(".", "•").replace("-", "—")

        self.output.delete("1.0", END)
        self.output.insert(END, pretty)

        self.history.append(f"{text} → {pretty}")

        self.history_box.delete("1.0", END)

        for i in range(len(self.history)):
            self.history_box.insert(
                END,
                f"{i+1}. {self.history[i]}\n"
            )

    def clear(self):
        self.entry.delete(0, END)
        self.output.delete("1.0", END)


root = Root()
root.mainloop()