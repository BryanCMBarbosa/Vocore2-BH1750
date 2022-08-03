import smbus

class bh1750():
  def __init__(self, address = 0x23): #can use 0x5c
    self.bus = smbus.SMBus(0)
    self.device_address = address
    self.read_ids = {"o_low": 0x23, "o_high_1": 0x21, "o_high_0.5":0x20, "c_low": 0x13, "c_high_1": 0x10, "c_high_0.5": 0x11}

  def read_raw_data(self, mode):
    data = self.bus.read_i2c_block_data(self.device_address, self.read_ids[mode])
    return data

  def read_converted_data(self, mode):
    response = self.read_raw_data(mode)
    return ((response[1] + (256 * response[0])) / 1.2)