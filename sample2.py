#import math

class Channel_Manager:
    def __init__(self):
        self.multiChannel = 0

    def channel_subtract(self, channel_ID, value):
        """Subtract a value from the specified channel."""
        current_value = self.ChannelGetValue(channel_ID)
        current_value -= value
        if not self.ValidateValue(current_value): return
        self.ChannelSetValue(channel_ID, current_value)

    def Channel_Add(self, channel_ID, value) -> None:
        current_value = self.ChannelGetValue(channel_ID)
        current_value += value
        if not self.ValidateValue(current_value):return 
        self.ChannelSetValue(channel_ID, current_value)

    def ChannelSetValue(self, channelID, value):
        if not self.ValidateValue(value): return
        self.ChannelClear(channelID)
        value = value * (1000**(channelID - 1))
        self.multiChannel += value

    def ChannelClear(self, channelID):
        if channelID == -1:
            self.multiChannel = 0
        else:
            channelValue = self.ChannelGetValue(channelID)
            channelValue = channelValue * (1000**(channelID - 1))
            self.multiChannel -= channelValue

    def ValidateValue(self, value):
        if 0 < value < 999:
            return True
        print("Value out of range, operation not performed")
        return False

    def display_all_channels(self) -> None:
        """Display the values of all three channels."""
        value = self.ChannelGetValue(1)
        print(f"Channel 1 is {value}")
        value = self.ChannelGetValue(2)
        print(f"Channel 2 is {value}")
        value = self.ChannelGetValue(3)
        print(f"Channel 3 is {value}")

    def ChannelGetValue(self, channelID):
        result = self.multiChannel % (1000**channelID) // (1000**(channelID - 1))
        return result

channel_manager = Channel_Manager()


###DO NOT ALTER ANY CODE BELOW THIS LINE###

def main():
    #channel_manager.multiChannel = 123456789
    channel_manager.ChannelSetValue(2,555)
    channel_manager.channel_subtract(2,111)
    channel_manager.display_all_channels()
    channel_manager.ChannelClear(-1)
    channel_manager.channel_subtract(3,1)
    channel_manager.ChannelSetValue(1,111)
    channel_manager.ChannelSetValue(2,888)
    channel_manager.display_all_channels()
    channel_manager.channel_subtract(1,111)
    channel_manager.Channel_Add(2,111)
    #channel_manager.Channel_Add(3,5555)
    #channel_manager.display_all_channels()





#Start the program
if __name__ == "__main__":
    main()

print("Program terminated")
