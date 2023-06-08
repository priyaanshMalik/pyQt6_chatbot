from multiprocess import Process
import model_query as bot
import loading
import viewController as vc

if __name__ == "__main__":

    def child_process():
        loading.runLoad()

    p1 = Process(target=child_process)
    p1.start()
    botObj = bot.setup()
    p1.join()
    vc.GUI(botObj)
