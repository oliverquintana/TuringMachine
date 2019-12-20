def read_rules(path = "rules.txt"):
    f = open(path, "r").read()
    r = eval(f)

    return r

class Tape(object):

    def __init__(self, input_tape = ['B'], head_pos = 0):
        self.tape = input_tape
        self.head_pos = head_pos

    def move_left(self):
        """
        Indica al cabezal que el siguiente movimiento debe realizarse a la izquierda.
        Si se encuentra en la posición inicial, una alerta es mostrada, indicando que 
        el movimiento es no válido.
        """
        if self.head_pos < 1:
            return False 
            raise Exception("Invalid Movement")
        else:
            self.head_pos -= 1
            return True 

    def move_right(self):
        """
        Indica al cabezal que el siguiente movimiento debe realizarse a la derecha.
        Al realizar este movimiento se agrega una celda con la cadena vacía una
        posición más allá de la que se está realizando el movimiento, dando así
        la interpretación de una cinta infinita.
        """
        if self.head_pos == len(self.tape) - 1:
            self.tape.append('B')

        self.head_pos += 1

    def get_tape(self):
        """
        Devuelve la cinta en el momento dado.
        """
        return self.tape

    def head_position(self):
        """
        Devuelve la posición en la que se encuetra el cabezal con respecto a la cinta.
        """
        return self.head_pos

    def read(self):
        """
        Lectura del símbolo en la posición actual del cabezal en la cinta.
        """
        return self.tape[self.head_pos]

    def write(self, value):
        """
        Reemplaza el caracter en la posición actual del cabezal en la cinta por el valor que
        contiene la variable de entrada "value"
        """
        self.tape[self.head_pos] = value

    def isEmpty(self):
        for i in self.tape:
            if i != None:
                return False
        return True

    def go_to(self, position = 0):
        if self.head_pos == position:
            return True
        elif self.head_pos < position:
            while self.head_pos < position:
                self.move_right()
            return True

        return flag

class TM(object):

    def __init__(self, current_state = 'q0', next_state = None, rules = None, input_tape = [None], algorithm = None):

        self.next_state = next_state
        self.rules = rules
        self.tape = Tape(input_tape)
        self.current_state = current_state
        self.algorithm = algorithm

    def run(self):
        """
        Función para comenzar la simulación de la Máquina de Turing.
        Lee las reglas desde un archivo de texto.
        """

        print("Start")

        algorithm = " "

        f = open ("tape.txt", "w+")
        f.write("Turing Machine: {}".format(self.algorithm))
        f.write("\nInput tape: {}".format(self.tape.get_tape()))
        counter = 0

        #f.write("\n{}".format(self.rules))

        while self.rules.get(self.current_state)[0] != 'Final':

            # Possibilities for current state
            possibilities = self.rules.get(str(self.get_current_state()))
            flag = True

            for i in possibilities:

                if i[0] == self.tape.read():
                    # Set next state
                    self.set_next_state(i[1])
                    # Write value in tape
                    self.tape.write(i[2])
                    # Move head to position
                    if i[3] == 'R':
                        self.tape.move_right()
                    else:
                        temp = self.tape.move_left()
                        if temp == False:
                            return "ExcInvMov"
                    # Set next state
                    f.write("\nTape: {}, current_state: {}, next_state: {}, head_pos: {}".format(self.tape.get_tape(), self.current_state, self.next_state,self.tape.head_pos))
                    print("Tape: {}, current_state: {}, next_state: {}, head_pos: {}".format(self.tape.get_tape(), self.current_state, self.next_state,self.tape.head_pos))
                    self.update_current_state()
                    counter += 1
                    flag = False
                    break

            if flag == True:
                f.close()
                f = open("tape.txt", "w+")
                f.close()
                return "ExcNonSta"
                raise Exception("Non end state reached")

        if self.rules.get(self.current_state)[0] == 'Final':
            print("End State Reached")
            return ""
            return True 
        else:
            raise Exception("Iterations Exceeded")

        return

    def get_current_state(self):
        """
        Identifica el estado actual dentro de la simulación.
        """
        return self.current_state

    def update_current_state(self):
        """
        Actualiza el estado actual por el estado siguiente dadas las condiciones
        en las reglas cargadas.
        """
        self.current_state = self.next_state
        self.next_state = None

    def get_next_state(self):
        """
        Obtiene el estado siguiente al actual.
        """
        return self.next_state

    def set_next_state(self,value):
        """
        Indica el estado siguiente al actual.
        """    
        self.next_state = value

    def get_rules(self):
        """
        Muestra las reglas cargadas.
        """
        return self.rules

if __name__ == '__main__':

    tape = [0,0,1,1]
    a = Tape(tape)
    a.write('a')
    print(a.get_tape())
