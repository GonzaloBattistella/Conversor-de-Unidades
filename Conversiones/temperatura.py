#######################################
#Funciones Celsius (°C)
def celsius_a_fahrenheit(celsius):
  return (celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
  return celsius + 273.15

def celsius_a_rankine(celsius):
  return (celsius + 273.15) * 9/5

def celsius_a_reaumur(celsius):
  return celsius * 4/5

#######################################
#Funciones Fahrenheit (°F)
def fahrenheit_a_celsius(fa):
  return (fa - 32) * 5/9

def fahrenheit_a_kelvin(fa):
  return (fa + 459.67) * 5/9

def fahrenheit_a_rankine(fa):
  return fa + 459.67

def fahrenheit_a_reaumur(fa):
  return (fa - 32) * 4/9

#######################################
#Funciones Kelvin (°K)
def kelvin_a_celsius(K):
  return K - 273.15

def kelvin_a_fahrenheit(K):
  return (K * 9/5) - 459.7

def kelvin_a_rankine(K):
  return K * 9/5

def kelvin_a_reaumur(K):
  return (K -  273.15) * 4/5

#######################################
#Funciones Rankine (°R)
def rankine_a_celsius(R):
  return (R - 491.67) * 5/9

def rankine_a_fahrenheit(R):
  return R - 459.67

def rankine_a_kelvin(R):
  return R - 5/9

def rankine_a_reaumur(R):
  return ((R - 491.67) * 5/9) * 4/5

#######################################
#Funciones Réaumur (°Ré)
def reaumur_a_celsius(Re):
  return Re * 5/4

def reaumur_a_fahrenheit(Re):
  return (Re * 9/4) + 32 

def reaumur_a_kelvin(Re):
  return (Re * 5/4) + 273.15

def reaumur_a_rankine(Re):
  return ((Re * 5/4) + 273.15) * 9/5