from Utils import Utils
import easyocr


test = Utils()


def main():
    test.upgrade('elixir', (56, 77, 78))

# def main():
#     test.formTroop()

# def main():
#     test.upgrade('elixir', (161, 226, 255))

# def main():
#     reader = easyocr.Reader(['en'])
#     result = reader.readtext('build/elixir_amount_screen.png')
#     print(result)

    #afficher juste le texte



    # for (bbox, text, prob) in result:
    #     print(text)




if __name__ == '__main__':
    main()