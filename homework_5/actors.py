actors = ["Elizabeth Taylor",
          "27 February 1932 – 23 March 2011,",
          "British and American actress. ",


          "Marlon Brando",
          "April 3, 1924 – July 1, 2004",
          "American actor and activist. ",


          "Marilyn Monroe ",
          "June 1, 1926 – August 4, 1962",
          "American actress and model."

          ]
name = input("Enter actor's name/lastname: ").capitalize()

for i in actors:
    if name in i:
        n = actors.index(i)
        for k in range (n,n+3):
            print(actors[k])
