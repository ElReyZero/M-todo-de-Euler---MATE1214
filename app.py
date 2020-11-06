"""
 * Desarrolado para el curso MATE1214 - Cálculo Integral con Ecuaciones Diferenciales
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 * Contribución de:
 *
 * Juan Andrés Romero Colmenares - 202013449
 *
 """

from matplotlib import pyplot as plt
import numpy
import math
import sys

def euler(fun, xStart, yStart, xEnd, stepsize, orf):
    """Esta función calcula la solución a una ecuación diferencial usando el método de euler

    Args:
        fun ([str]): Ecuación diferencial
        xStart ([float]): valor del x inicial
        yStart ([float]): valor del y inicial
        xEnd ([float]): valor del x final
        stepsize ([float]): tamaño de paso
        orf ([str]): String de la ec diferencial original
    """
    x, y = xStart, yStart
    xlist, ylist = [], []
    while x <= xEnd:
        xlist.append(x)
        ylist.append(y)

        y += stepsize * eval(fun)
        x += stepsize

    plt.title('Aproximación a la ecuación {0}'.format(orf))
    plt.plot(xlist, ylist)
    plt.show()

def replaceEval(fun):
    """Esta función reemplaza strings por operaciones legibles por eval()

    Args:
        fun ([str]): Ecuación diferencial

    Returns:
        fun ([str]): Ecuación diferencial con parámetros evaluables.
        ofc ([str]): Ecuación diferencial original.
    """

    ofc = fun
    fun = fun.replace("^", "**")
    fun = fun.replace("euler", "math.exp(1)")
    fun = fun.replace("pi", "math.pi")
    fun = fun.replace("sen", "math.sin")
    fun = fun.replace("cos", "math.cos")
    fun = fun.replace("tan", "math.tan")
    fun = fun.replace("arctan", "math.atan")
    fun = fun.replace("arcsen", "math.asen")
    fun = fun.replace("arccos", "math.acos")
    fun = fun.replace("senh", "math.sinh")
    fun = fun.replace("cosh", "math.cosh")
    fun = fun.replace("tanh", "math.tanh")
    return fun, ofc
 
def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Calcular solución a una ecuación diferencial")
    print("0- Salir")
    print("*******************************************")

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')
    if int(inputs[0]) == 1:
        print("\n- Cómo ingresar la ecuación:")
        print("- Ingresar el número e como la palabra 'euler'.")
        print("- Ingresar el número pi como la palabra 'pi'.")
        print("- Las multiplicaciones deben escribirse explícitamente con *.")
        print("- Ej: 3x se escribe como 3*x")
        print("- Asegurarse de cerrar todos los paréntesis.")
        print("  (Si no lo hace podría obtener resultados equivocados).")
        print("- Este programa soporta funciones trigonométricas e hiperbólicas.")
        print("- Para escribir secante, cosecante o cotangente ingrese función de la forma (1/f(x)).\n")
        fun = input("Ingrese la ecuación diferencial: ")
        fun, ofc = replaceEval(fun)
        xStart = float(input("Ingrese la coordenada x inicial: "))
        yStart = float(input("Ingrese la coordenada y inicial: "))
        xEnd = float(input("Ingrese La coordenada x final: "))
        stepsize = float(input("Ingrese el tamaño de paso: "))
        euler(fun, xStart, yStart, xEnd, stepsize, ofc)
    else:
        sys.exit(0)
sys.exit(0)

