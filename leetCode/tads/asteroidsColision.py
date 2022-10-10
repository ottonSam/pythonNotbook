inputVar = [5,10,-5]

def asteroidsColision(asteroids):
        originalLen = len(asteroids)
        while(True):
            colision = False
            for i in range(len(asteroids) - 1):
                if asteroids[i] > 0 and asteroids[i+1] < 0:
                    if asteroids[i] == abs(asteroids[i+1]):
                        del asteroids[i:i+2]
                        colision = True
                        break
                    elif asteroids[i] > abs(asteroids[i+1]):
                        del asteroids[i+1]
                        colision = True
                        break
                    elif asteroids[i] < abs(asteroids[i+1]):
                        del asteroids[i]
                        colision = True
                        break
            if not colision:
                return(asteroids)

print(asteroidsColision(inputVar))