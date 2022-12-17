print('[WELCOME IN GUESSING GAME]\nIn this game you have to guess number which is pre-defined...\n All THE BEST...')
n=int(input("Enter Your Number.."))
k=5
i=0
while i==0:
    if n==3:
        print("Nice..YOU GET 3 chance for guessing the number")
        r=1
        while r<=3:
            q=int(input("enter number again "))
            if q==5:
                print(q,"{congratulations.. You Are Winner...}")
            else:
                print(q,"{Ahh..No you loss}")
            r+=1
            
    elif k==n:
        print(n,"{congratulations.. You Are Winner...}")
    else:
        print("{SORRY YOU LOSS...PLEASE PLAY AGAIN}")
    i+=1