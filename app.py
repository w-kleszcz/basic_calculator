"""Module providing a simple calculator functionality."""
from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/calculate')
def hello_world():  # put application's code here
    """Main calculator function."""
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    res = ''
    op_str = ''
    match op:
        case 'sum':
            res = str(arg1 + arg2)
            op_str = ' + '
        case 'sub':
            res = str(arg1 - arg2)
            op_str = ' - '
        case 'mul':
            res = str(arg1 * arg2)
            op_str = ' * '
        case 'div':
            if arg2 != 0:
                res = str(arg1 / arg2)
            else:
                res = 'error! division by zero!'
            op_str = ' / '

    return str(arg1) + op_str + str(arg2) + ' = ' + res



if __name__ == '__main__':
    app.run()
