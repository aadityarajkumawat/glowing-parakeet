from statemachine import StateMachine, State
import tkinter as tk

class VendingMachine(StateMachine):
  coke = State("CocaCola", initial=True)
  sprite = State("Sprite")
  fanta = State("Fanta")
  pepsi = State("Pepsi")

  select_sprite = coke.to(sprite)
  select_fanta = coke.to(fanta)
  select_pepsi = coke.to(pepsi)

  select_coke_sprite = sprite.to(coke)
  select_coke_fanta = fanta.to(coke)
  select_coke_pepsi = pepsi.to(coke)

  def reset_state(self):
    if(VendingMachine.sprite == self.current_state):
      self.select_coke_sprite()
    elif(VendingMachine.fanta == self.current_state):
      self.select_coke_fanta()
    elif(VendingMachine.pepsi == self.current_state):
      self.select_coke_pepsi()

def vendCurrentDrink(drink_name):
  for i in (drinks):
    if(i == drink_name):
      drinks[i]["qty"] = drinks[i]["qty"] - 1

drinks = {"coke": {"qty": 5, "price": 35},
          "sprite": {"qty": 5, "price": 30},
          "fanta": {"qty": 5, "price": 40},
          "pepsi": {"qty": 5, "price": 45}}

vending_machine = VendingMachine()

wallet = 1000

enteredAmout = 10
changeAmount = 0

if(drinks[vending_machine.current_state.identifier]["qty"] > 0):
  if(drinks[vending_machine.current_state.identifier]["price"] <= enteredAmout):
    wallet = wallet - enteredAmout
    vendCurrentDrink(vending_machine.current_state.identifier)
    changeAmount = enteredAmout - drinks[vending_machine.current_state.identifier]["price"]
  else:
    drink_name = vending_machine.current_state.identifier
    drink_price = drinks[drink_name]["price"]
    vending_machine.reset_state()
else:
  drink_name = vending_machine.current_state.identifier
  vending_machine.reset_state()
    
# GUI

root = tk.Tk()
root.title("Vending Machine")
root.configure(background='#212121')
root.geometry('1200x800')

top_frame = tk.Frame(root)
top_frame.configure(background='#212121')
top_frame.pack(fill=tk.X)


wallet_btn = tk.Label(top_frame, text='Wallet: 1000', fg='#fff', height='2', width='14')
wallet_btn["bg"] = "#727272"
wallet_btn["border"] = 0 
wallet_btn.pack(side=tk.LEFT, padx=20, pady=20)

title = tk.Label(top_frame, text='Vending Machine', fg='#ffffff', font=20)
title.configure(background='#212121')
title.pack(pady=20, padx=100)

# Client wallet

wallet_amt = 1000

# Function

price_color_coke='#fff'
price_color_sprite='#fff'
price_color_fanta='#fff'
price_color_pepsi='#fff'

def got30():
  givencost = 30

  if(vending_machine.current_state.value == 'coke'):
      changeAmount = givencost - 35
  elif(vending_machine.current_state.value == 'sprite'):
    changeAmount = givencost - 30
  elif(vending_machine.current_state.value == 'fanta'):
    changeAmount = givencost - 40
  elif(vending_machine.current_state.value == 'pepsi'):
    changeAmount = givencost - 45
  if(changeAmount < 0):
    vending_machine.reset_state()
  cc = 'Change: ' + str(changeAmount)
  change_label.configure(text=cc)

def got40():
  givencost = 40
  if(vending_machine.current_state.value == 'coke'):
      changeAmount = givencost - 35
  elif(vending_machine.current_state.value == 'sprite'):
    changeAmount = givencost - 30
  elif(vending_machine.current_state.value == 'fanta'):
    changeAmount = givencost - 40
  elif(vending_machine.current_state.value == 'pepsi'):
    changeAmount = givencost - 45
  if(changeAmount < 0):
    vending_machine.reset_state()
  cc = 'Change: ' + str(changeAmount)
  change_label.configure(text=cc)

def got50():
  givencost = 50
  if(vending_machine.current_state.value == 'coke'):
      changeAmount = givencost - 35
  elif(vending_machine.current_state.value == 'sprite'):
    changeAmount = givencost - 30
  elif(vending_machine.current_state.value == 'fanta'):
    changeAmount = givencost - 40
  elif(vending_machine.current_state.value == 'pepsi'):
    changeAmount = givencost - 45
  if(changeAmount < 0):
    vending_machine.reset_state()
  cc = 'Change: ' + str(changeAmount)
  change_label.configure(text=cc)

def selectCoke():
  vending_machine.reset_state()
  coke_price_label.configure(fg='red')
  sprite_price_label.configure(fg='#fff')
  fanta_price_label.configure(fg='#fff')
  pepsi_price_label.configure(fg='#fff')
  curr_drink.configure(file='./assets/coke.png')
  thiscost = 35
  cc = 'Cost:' + str(thiscost)
  cost_label.configure(text=cc)

def selectSprite():
  vending_machine.reset_state()
  vending_machine.select_sprite()
  coke_price_label.configure(fg='#fff')
  sprite_price_label.configure(fg='lightgreen')
  fanta_price_label.configure(fg='#fff')
  pepsi_price_label.configure(fg='#fff')
  curr_drink.configure(file='./assets/sprite.png')
  thiscost = 30
  cc = 'Cost:' + str(thiscost)
  cost_label.configure(text=cc)

def selectFanta():
  vending_machine.reset_state()
  vending_machine.select_fanta()
  coke_price_label.configure(fg='#fff')
  sprite_price_label.configure(fg='#fff')
  fanta_price_label.configure(fg='orange')
  pepsi_price_label.configure(fg='#fff')
  curr_drink.configure(file='./assets/fanta.png')
  thiscost = 40
  cc = 'Cost:' + str(thiscost)
  cost_label.configure(text=cc)

def selectPepsi():
  vending_machine.reset_state()
  vending_machine.select_pepsi()
  coke_price_label.configure(fg='#fff')
  sprite_price_label.configure(fg='#fff')
  fanta_price_label.configure(fg='#fff')
  pepsi_price_label.configure(fg='#0066ff')
  curr_drink.configure(file='./assets/pepsi.png')
  thiscost = 45
  cc = 'Cost:' + str(thiscost)
  cost_label.configure(text=cc)

def pay():
  global wallet_amt
  if(vending_machine.current_state.value == 'coke'):
      wallet_amt = wallet_amt - 35
  elif(vending_machine.current_state.value == 'sprite'):
    wallet_amt = wallet_amt - 30
  elif(vending_machine.current_state.value == 'fanta'):
    wallet_amt = wallet_amt - 40
  elif(vending_machine.current_state.value == 'pepsi'):
    wallet_amt = wallet_amt - 45

  ww = "Wallet: " + str(wallet_amt)
  wallet_btn.configure(text=ww)

def clean_reset():
  global wallet_amt
  vending_machine.reset_state()
  vending_machine.select_pepsi()
  coke_price_label.configure(fg='#fff')
  sprite_price_label.configure(fg='#fff')
  fanta_price_label.configure(fg='#fff')
  pepsi_price_label.configure(fg='#fff')
  curr_drink.configure(file='./assets/fil.png')
  cost_label.configure(text='Cost: ...')
  change_label.configure(text='Change: ...')
  wallet_btn.configure(text='Wallet: 1000')
  wallet_amt = 1000
  wallet = 1000

# Drinks Frame

drinks_frame = tk.Frame(root)
drinks_frame.configure(background='#989898', width='800', height='200')
drinks_frame.pack(pady=20)

# Drinks

drink_coke = tk.Frame(drinks_frame)
drink_coke.configure(background='#4a4a4a', width='200', height='200')
drink_coke.grid(column=0, row=0, padx=2, pady=2)

coke_img = tk.PhotoImage(file='./assets/coke.png')
coke_label = tk.Button(drink_coke, image=coke_img, bg='#4a4a4a', height='200', width='200', borderwidth=1, command=selectCoke)
coke_label.pack()

drink_sprite = tk.Frame(drinks_frame)
drink_sprite.configure(background='#4a4a4a', width='200', height='200')
drink_sprite.grid(column=1, row=0, padx=2, pady=2)

sprite_img = tk.PhotoImage(file='./assets/sprite.png')
sprite_label = tk.Button(drink_sprite, image=sprite_img, bg='#4a4a4a', height='200', width='200', borderwidth=1, command=selectSprite)
sprite_label.pack()

drink_fanta = tk.Frame(drinks_frame)
drink_fanta.configure(background='#4a4a4a', width='200', height='200')
drink_fanta.grid(column=2, row=0, padx=2, pady=2)

fanta_img = tk.PhotoImage(file='./assets/fanta.png')
fanta_label = tk.Button(drink_fanta, image=fanta_img, bg='#4a4a4a', height='200', width='200', borderwidth=1, command=selectFanta)
fanta_label.pack()

drink_pepsi = tk.Frame(drinks_frame)
drink_pepsi.configure(background='#4a4a4a', width='200', height='200')
drink_pepsi.grid(column=3, row=0, padx=2, pady=2)

pepsi_img = tk.PhotoImage(file='./assets/pepsi.png')
pepsi_label = tk.Button(drink_pepsi, image=pepsi_img, bg='#4a4a4a', height='200', width='200', borderwidth=1, command=selectPepsi)
pepsi_label.pack()

# Drink price labels

price_labels_frame = tk.Frame(root)
price_labels_frame.configure(background='#989898', width='825', height='40')
price_labels_frame.pack()

k = '29'

coke_price_label = tk.Label(price_labels_frame, text='35', bg='#4a4a4a', fg=price_color_coke, height='2', width=k, borderwidth=1)
coke_price_label.grid(column=0, row=0)

sprite_price_label = tk.Label(price_labels_frame, text='30', bg='#4a4a4a', fg=price_color_sprite, height='2', width=k, borderwidth=1)
sprite_price_label.grid(column=1, row=0)

fanta_price_label = tk.Label(price_labels_frame, text='40', bg='#4a4a4a', fg=price_color_fanta, height='2', width=k, borderwidth=1)
fanta_price_label.grid(column=2, row=0)

pepsi_price_label = tk.Label(price_labels_frame, text='45', bg='#4a4a4a', fg=price_color_pepsi, height='2', width=k, borderwidth=1)
pepsi_price_label.grid(column=3, row=0)

# Select coin

spec_frame = tk.Frame(root)
spec_frame.configure(width='825', height='300', background='#212121')
spec_frame.pack(pady=30)

# Insert coin frame

insert_coin = tk.Frame(spec_frame)
insert_coin.configure(width='300', height='300', background='#212121')
insert_coin.grid(column=0, row=0)

insert_c = tk.Label(insert_coin)
insert_c.configure(width='42', text='Insert Coin', background='#212121', fg='#fff', font=8)
insert_c.grid(column=0, row=0, pady=30)

list_frame = tk.Frame(insert_coin)
list_frame.configure(width='300', height='278', background='#212121')
list_frame.grid(column=0, row=1)
h = '1'
coin_color_30 = "#fff"
coin_color_40 = "#fff"
coin_color_50 = "#fff"
coin1 = tk.Button(list_frame, text='30', width='12', height=h, fg=coin_color_30, bg='#212121', font=8, command=got30)
coin1.grid(column=0, row=0, pady=2)

coin2 = tk.Button(list_frame, text='40', width='12', height=h, fg=coin_color_40, bg='#212121', font=8, command=got40)
coin2.grid(column=0, row=1, pady=2)

coin3 = tk.Button(list_frame, text='50', width='12', height=h, fg=coin_color_50, bg='#212121', font=8, command=got50)
coin3.grid(column=0, row=2, pady=2)

pay_btn = tk.Button(list_frame, text='Pay', background='#0066ff', fg='#fff', width='32', border='0', height='3', command=pay)
pay_btn.grid(pady=10)

reset_btn = tk.Button(list_frame, text='Reset', background='#0066ff', fg='#fff', width='32', border='0', height='3', command=clean_reset)
reset_btn.grid(pady=10)

dark='#212121'
light='#fff'

# Filler

filler = tk.Frame(spec_frame)
filler.configure(width='225', height='300', background='#212121')
filler.grid(column=1, row=0)

# Current product

insert_coin1 = tk.Frame(spec_frame)
insert_coin1.configure(width='300', height='300', background=dark)
insert_coin1.grid(column=2, row=0)

cost_label = tk.Label(insert_coin1, text='Cost: ...', width='42', background=dark, fg=light, font=8)
cost_label.grid(column=0, row=0, pady=3)
change_label = tk.Label(insert_coin1, text='Change: ...', width='42', background=dark, fg=light, font=8)
change_label.grid(column=0, row=1, pady=3)

curr_drink = tk.PhotoImage(file='./assets/fil.png')

curr_drink_label = tk.Label(insert_coin1, image=curr_drink, background='#3a3a3a')
curr_drink_label.grid()

root.mainloop()
