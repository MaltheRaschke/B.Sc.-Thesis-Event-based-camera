#!/usr/bin/env python

import rospy
import pickle
import csv

from std_msgs.msg import String
from event_pack.msg import Event

def event_callback(event, csv_writer):
    # Callback function to handle incoming events
    # Here you can process the event data as per your requirement
    # For now, let's assume you want to save the data using pickle
    row = [event.timestamp, event.x_cord, event.y_cord, event.polarity]
   
    csv_writer.writerow(row)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", row)


def event_subscriber():
    # Initialize the ROS node
    rospy.init_node('event_subscriber', anonymous=True)

    # Create a CSV file and writer
    csv_file = open('/path/to/target/folder/event_data.csv', 'w')
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(['X', 'Y', 'Polarity', 'Timestamp'])

    # Create a subscriber
    rospy.Subscriber('talker', Event, event_callback, callback_args=csv_writer)

    # Spin the node to receive events
    rospy.spin()

    # Close the CSV file
    csv_file.close()

if __name__ == '__main__':
    try:
        event_subscriber()
    except rospy.ROSInterruptException:
        pass
