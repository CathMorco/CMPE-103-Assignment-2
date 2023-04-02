import pygame

W, H = 800, 600

#Creates the display screen
display = pygame.Surface ((W, H))
screen = pygame.display.set_mode ((W, H))
pygame.display.set_caption("Decryption")
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

#Asks the user for the statement that will be decrypted
string=input(str("Please Input your statement:"))

#Converts the following characters: 'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !
new_string= (string.replace("*","a").replace("&","e").replace("#","i").replace("+","o").replace("!","u"))
print("\n Now look back again at the 'Decryption' display screen :D")

# Split into words
words = new_string.split()

# Calculate number of words per line
num_words = len(words)
words_per_line = num_words // 3

# Divide into 3 lines
line1 = " ".join(words[:words_per_line])
line2 = " ".join(words[words_per_line:2*words_per_line])
line3 = " ".join(words[2*words_per_line:])

#Combines the 3 lines into one list
texts= [line1,line2,line3]


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