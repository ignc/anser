#!/usr/bin/env python
# -*- coding: utf-8 -*-

from anser import Anser


server = Anser(__name__, debug=True)

@server.action('default')
def action_a(message, address):
    print("{0} - {1}".format(address, message))


if __name__ == '__main__':
    server.run()
