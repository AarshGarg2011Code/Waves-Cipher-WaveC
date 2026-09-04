import matplotlib.pyplot as plt

def plot_text_ascii(text):
    chars = list(text)
    ascii_values = [ord(c) for c in chars]
    x = range(len(chars))
    plt.figure()
    plt.plot(x, ascii_values, marker='o')
    plt.xticks(x, chars)
    plt.xlabel("Characters")
    plt.ylabel("ASCII Value")
    plt.title("Character vs ASCII Graph")
    plt.grid(True)
    plt.show()
    print(ascii_values)
