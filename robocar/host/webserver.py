import bottle
from robocar.host import mqtt_publisher as mp

bottle.app = bottle.Bottle()

STATIC_DIR = 'robocar/host/static'
SERVER = '192.168.0.31'
PORT = 8080


# serve static
@bottle.app.route('/static/<path:path>')
def serve_static(path):
    filename = path
    return bottle.static_file(filename, root=STATIC_DIR)


@bottle.app.route('/')
def index():
    with open('robocar/host/index.html') as f:
        data = f.read()
        return data


@bottle.app.route('/motors/<direction>')
def control(direction):
    mp.publish_msg(direction)


def main():
    bottle.app.run(host=SERVER, port=PORT)


if __name__ == "__main__":
    main()
