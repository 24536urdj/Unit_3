###
     def produce(n = 100) -> object:
      x_out = []
      y_out = []

      st = -10
      for i in range(100):
          x = -st
          x_out.append(x)
          y = abs(x)
          y_out.append(y)
          y_str = f"{y:.2f}"
          st += 0.2
          print(f"|{str(x).center(10)}|{y_str.center(10)}")

      return y_out, x_out


    sample = produce(n=100)

    from matplotlib import pyplot as plt

    data_y, data_x = produce(n=100)
    plt.plot(data_x, data_y, color="yellow", marker="*")
    plt.xlabel("Variable x")
    plt.ylabel("$y=2*(x+5)**2}$")
    plt.show()
    
   ![](https://github.com/24536urdj/Unit_3/blob/main/quiz/Screen%20Shot%202023-01-11%20at%2020.56.20.png)
    
    
