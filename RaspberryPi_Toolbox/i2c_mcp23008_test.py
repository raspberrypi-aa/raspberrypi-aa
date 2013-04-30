#!/usr/bin/env python
#
# Uses the MCP23008 I2C GPIO Expander 
#
#

mcp = Adafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)

mcp.config(0, OUTPUT)
mcp.output(0, 1)