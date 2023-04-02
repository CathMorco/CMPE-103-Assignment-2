#Morco, Cathleen Jan M., BSCPE 1-5 , 04/02/2023
#A program that uses The Vigenère Cipher

import pygame

W, H = 800, 600

#Creates the display screen
display = pygame.Surface ((W, H))
screen = pygame.display.set_mode ((W, H))
pygame.display.set_caption("Vigenère Cipher")
clock = pygame.time.Clock()

#RGB example values
black = (0,0,0)
white = (255,255,255)

#The rate of change in colors
col_spd = 1

#The color directory & its values
col_dir =[[-1,1,1],[-1,1,-1],[-1,1,1],[-1,1,-1]]
def_col = [[120,120,240],[140,140,240],[160,160,220]]

#Initialized values for functions
minimum = 0
maximum = 255

#Draws the text
def draw_text(text, size, col, x, y):
    font = pygame.font.get_default_font()
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, col)
    text_rect=text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface, text_rect)

#Creates the color change
def col_change(col,dir):
    for i in range(1):
        col[i] += col_spd * dir[i]
        if col[i] >=maximum or col[i] <=minimum:
            dir[i] *= -1

#Combines the color change and draw text into one function
def array_func(col,dir,text,size,x,y):
    for i in range(len(col)):
        draw_text(text[i],size,col[i],x,y + i*50)
        col_change(col[i],dir[i])


pygame.init()

# Ask for user input
message = input("Please insert your plaintext: ").lower().replace(" ", "")
keyword = input("Please insert your keyword: ").lower().replace(" ", "")

# Make sure the keyword is long enough
while len(keyword) < len(message):
    keyword += input("Please enter your keyword again until it has met the quota: ").lower()
    keyword = keyword[:len(message)]

# Encrypt the message
cipher_text = []
for i in range(len(message)):
    messageConstant = ord(message[i]) - 97
    keywordConstant = ord(keyword[i]) - 97
    cipherConstant = (messageConstant + keywordConstant) % 26
    cipher_text.append(chr(cipherConstant + 65))

# Format the ciphertext into three lines
num_words = len(cipher_text)
words_per_line = num_words // 3
line1 = " ".join(cipher_text[:words_per_line])
line2 = " ".join(cipher_text[words_per_line:2*words_per_line])
line3 = " ".join(cipher_text[2*words_per_line:])
texts= [line1,line2,line3]

print("\n Now look back again at the 'Vigenère Cipher' display screen :D")

run=True

#Runs the program
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    array_func(def_col,col_dir,texts,40, W / 2 , 200)

    clock.tick()

    display.blit(screen,(0,0))
    pygame.display.update()