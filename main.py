from Tkinter import *
import irrf

class Window(object):

	def __init__(self, toplevel):
		self.toplevel = toplevel
		self.toplevel.geometry("360x220")
		self.frame_um = Frame(self.toplevel).grid()
		self.lblRemuneracao = Label(self.frame_um, text="Remuneracao")
		self.entryRemuneracao = Entry(self.frame_um, bg="white", width=40)
		self.lblDependente = Label(self.frame_um, text="Dependente")
		self.entryDependente = Entry(self.frame_um, bg="white", width=40)
		self.lblInss = Label(self.frame_um, text="Inss")
		self.entryInss = Entry(self.frame_um, bg="white", width=40)
		self.lblIrrf = Label(self.frame_um, text="Irrf")
		self.lblIrrf_2 = Label(self.frame_um, bg="gray", width=34)
		self.btn = Button(self.frame_um, text='Calcular', command=lambda:self.calculo())
		
		self.lblRemuneracao.grid(row=1, padx=10, pady=10, sticky=W)
		self.entryRemuneracao.grid(row=1, column=1, padx=10, pady=10)
		self.lblDependente.grid(row=2, padx=10, pady=10, sticky=W)
		self.entryDependente.grid(row=2, column=1, padx=10, pady=10)
		self.lblInss.grid(row=3, padx=10, pady=10, sticky=W)
		self.entryInss.grid(row=3, column=1, padx=10, pady=10)
		self.lblIrrf.grid(row=4, padx=10, pady=10, sticky=W)
		self.lblIrrf_2.grid(row=4, column=1, padx=10, pady=10)
		self.btn.grid(row=5, column=0, columnspan=2, padx=150, pady=10, sticky=E+W+S+N)

	def calculo(self):
		
		if self.entryRemuneracao.get() == "":
			a = irrf.ImpostoRenda()
			print 1
		elif self.entryDependente.get() == "" and self.entryInss.get() == "":
			a = irrf.ImpostoRenda(float(self.entryRemuneracao.get()))
			print 2
		elif self.entryDependente.get() == '':
			a = irrf.ImpostoRenda(float(self.entryRemuneracao.get()),0,float(self.entryInss.get()))
			print 3
		elif self.entryInss.get() == '':
			a = irrf.ImpostoRenda(float(self.entryRemuneracao.get()),float(self.entryDependente.get()), 0)
			print 4
		else:
			a = irrf.ImpostoRenda(float(self.entryRemuneracao.get()),float(self.entryDependente.get()),float(self.entryInss.get()))
			print 5
			
		self.lblIrrf_2['text'] = a.calculo()

quadro = Tk()
ex = Window(quadro)
quadro.mainloop()
