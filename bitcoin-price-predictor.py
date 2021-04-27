import tkinter as tk
import tkinter.messagebox

class BitCoinPredictor:
    
    def __init__(self,master):
        self.master = master
        self.master.title("CST2101 Lab 8")
        self.master.geometry("1200x360")
        self.CreateWidgets()
        
   
    def CreateWidgets(self):
        Frame1 = tk.Frame(self.master) #this is the first frame
        Frame1.grid()
        

        #this is for the title of the application
        self.mainLabel = tk.Label(Frame1, text="Bitcoin Price Predictor", bd=2, relief="solid", font=("Lucida Grande", 30, 'bold'), fg="black", bg="#e69900") 
        self.mainLabel.grid(row=0, column=1)
        
        #this is for the instructions
        self.instLabel = tk.Label(Frame1, text="Please, specify the following: ", font=("Lucida Grande", 20))
        self.instLabel.grid(row=1,column=1)
        
        user_name = tk.StringVar() #this is to declare user_name as a string variable
        current_price = tk.DoubleVar() #this is to declare current_price as an integer variable
        current_temperature = tk.DoubleVar() #this is to declare current_temperature as an integer variable
        predicted_price = tk.DoubleVar() #this is to declare the predicted price as a string variable
        
        #this is for the username label & entry
        self.userLabel = tk.Label(Frame1, text="Username:", font=("Lucida Grande", 18, 'bold'), fg="#663300")
        self.userLabel.grid(row=2, column=0)
        self.userEntry = tk.Entry(Frame1, textvariable=user_name)
        self.userEntry.grid(row=2, column=1)
        self.userEntry.config(width=33,relief=tk.RIDGE)
        
        #this is for the current price label & entry
        self.priceLabel = tk.Label(Frame1, text="Current Bitcoin Price:", font=("Lucida Grande", 18, 'bold'), fg="#663300")
        self.priceLabel.grid(row=3, column=0)
        self.priceEntry = tk.Entry(Frame1, textvariable=current_price)
        self.priceEntry.grid(row=3, column=1)
        self.priceEntry.config(width=33, relief=tk.RIDGE)
        
        #this is for the current temperature label & entry
        self.tempLabel = tk.Label(Frame1, text="Current Temperature (in celsius):", font=("Lucida Grande", 18, 'bold'), fg="#663300")
        self.tempLabel.grid(row=4, column=0)
        self.tempEntry = tk.Entry(Frame1, textvariable=current_temperature)
        self.tempEntry.grid(row=4,column=1)
        self.tempEntry.config(width=33, relief=tk.RIDGE)
        
        
        #this function handles the calculation for the predicted bitcoin price
        def predictPrice():
            present_price = current_price.get()
            present_temp = current_temperature.get()
            result = present_price * (1 + present_temp/100)
            
            predicted_price.set(result)
            
            #this is to display the username with the predicted price
            self.predictPriceLabel = tk.Label(Frame1, text=f"{user_name.get()}, bitcoin price of tomorrow will be: ${round(predicted_price.get(),2)}", font=("Lucida Grande", 18, 'bold'))
            self.predictPriceLabel.grid(row=7, column=1)
            return       
        
        #this function handles the reset of the application
        def Reset():
            user_name.set("")
            current_price.set(0)
            current_temperature.set(0)
            self.predictPriceLabel.config(text="")
            
             
        #this exits the aplication
        def Exit():
            master.destroy()
            return

        self.calcButton = tk.Button(Frame1, text="Calculate Price", font=("Lucida Grande", 12), bd=5, relief=tk.RAISED,padx=12, pady=12, command=predictPrice).grid(row=5, column=0)
        self.resetButton = tk.Button(Frame1, text="Reset", font=("Lucida Grande", 12), bd=5, relief=tk.RAISED, padx=12, pady=12, command=Reset).grid(row=5, column=1)
        self.exitButton = tk.Button(Frame1, text="Exit", font=("Lucida Grande", 12), bd=5, relief=tk.RAISED, padx=12, pady=12, command=Exit).grid(row=5, column=2)
        
if __name__ == '__main__':
    master = tk.Tk()
    app= BitCoinPredictor(master)
    master.mainloop()
    
        