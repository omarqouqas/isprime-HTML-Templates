from flask import Flask, request, render_template

app = Flask(__name__)


def is_prime(number):

    while True:
        try:
            if int(number) < 0:  # negative numbers are not prime
                return str(number) + " is not a Prime number because it is less than 0"
            if number == 2:  # 2 is considered as a prime number
                return str(number) + " is a Prime number."
            elif int(number) == 0 or int(number) == 1:
                return str(number) + " is not a Prime number."
            elif int(number) % 2 == 0 and int(number) != 2:
                return str(number) + " is not a Prime number because it is divisible by 2. " + str(number) +\
                       "/" + str(2) + " = " + str(int(number) / 2)
            elif int(number) > 3 and int(number) % 3 == 0:
                return str(number) + " is not a Prime number because it is divisible by 3. " + str(number) +\
                       "/" + str(3) + " = " + str(int(number) / 3)
            elif int(number) > 5 and int(number) % 5 == 0:
                return str(number) + " is not a Prime number because it is divisible by 5. " + str(number) +\
                       "/" + str(5) + " = " + str(int(number) / 5)
            elif int(number) > 7 and int(number) % 7 == 0:
                return str(number) + " is not a Prime number because it is divisible by 7. " + str(number) +\
                       "/" + str(7) + " = " + str(int(number) / 7)
            else:
                return str(number) + " is a Prime number because it is divisible by itself and 1"
        except ValueError:
            return str(number) + " is not a valid input. You need to enter an integer!"


@app.route("/", methods=['GET', 'POST'])
def index():

    number = None

    if request.method == 'POST':
        number = request.form['number']
        is_it_prime = is_prime(number)
        if is_it_prime:
            is_prime(number)
            number = {
                'number': number,
                'is_it_prime': is_prime(number)
            }
    return render_template('index.html', number=number, )


if __name__ == "__main__":
    app.run(host='127.0.0.14', port=8080, debug=True)
