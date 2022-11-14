import random
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def random_numero():
    n=random.sample(range(1,100), 10)
    n.sort()
    print(n)
random_numero()
def frase_letra():
    frase=int(input('dime una frase'))
    letra=int(input('dime que letra quieres buscar'))





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

