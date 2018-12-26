from lib.source import Source
from lib.model import Model
from lib.order import Order


sc = Source()

source = sc.read()

md = Model(source)

action = md.getAction()

od = Order()

od.send(action)
