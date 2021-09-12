available_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list', 'unordered-list']
whole_text = ""


def choose_a_formatter():
    global whole_text
    global request
    while True:
        request = input("Choose a formatter:")
        if request in available_formatters:
            if request == "bold":
                whole_text = whole_text + bold()
            elif request == "plain":
                whole_text = whole_text + plain()
            elif request == "italic":
                whole_text = whole_text + italic()
            elif request == "header":
                whole_text = whole_text + header()
            elif request == "link":
                whole_text = whole_text + link()
            elif request == "inline-code":
                whole_text = whole_text + inline_code()
            elif "order" in request:
                whole_text = whole_text + lists()
            elif request == "line-break":
                whole_text = whole_text + " "
            else:
                whole_text = whole_text + new_line()
            print(whole_text)
        elif request == "!done":
            with open('output.md', 'w') as text:
                text.write(whole_text)
                text.close()
            exit()
        elif request == "!help":
            help_me()
        else:
            print("Unknown formatting type or command")


def help_me():
    print("""Available formatters: plain bold italic header link inline-code new-line ordered-list unordered-list
Special commands: !help !done""")
    choose_a_formatter()


def bold():
    text = input("Text: ")
    return f"**{text}**"


def plain():
    text = input("Text: ")
    return f"{text}"


def italic():
    text = input("Text: ")
    return f"*{text}*"


def header():
    while True:
        level = int(input("Level: "))
        if level in range(1, 7):
            break
        else:
            print("The level should be within the range of 1 to 6")
            continue
    text = input("Text: ")
    return f"{level * '#'} {text}" + "\n"


def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def inline_code():
    code = input("Text: ")
    return f"`{code}`"


def new_line():
    return "\n"


def lists():
    list_items = ""
    while True:
        rows = int(input("Number of rows: "))
        if rows > 0:
            break
        print("The number of rows should be greater than zero")
    for i in range(rows):
        list_item = input(f'Row #{i + 1}: ')
        if request == "unordered-list":
            list_items = list_items + '* ' + list_item + '\n'
        else:
            list_items = list_items + f'{i + 1}. ' + list_item + '\n'
    return list_items


choose_a_formatter()
