from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_text_message, 

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_to_Start(self, event):
        return True
    
    # course
    def is_going_to_course(self, event):
        text = event.message.text
        return text.lower() == "課程"
    def is_going_to_add_course(self, event):
        text = event.message.text
        return text.lower() == "增加課程"
    def is_going_to_add_course_day(self, event):
        text = event.message.text
        return text.lower() == "增加星期幾的課程?"
    def is_going_to_add_course_item(self, event):
        text = event.message.text
        return text.lower() == "增加甚麼課程"
    
    def is_going_to_search_course(self, event):
        text = event.message.text
        return text.lower() == "查詢課程"
    def is_going_to_search_course_time(self, event):
        text = event.message.text
        return text.lower() == "查詢星期幾的課程呢?"
    
    def is_going_to_delete_course(self, event):
        text = event.message.text
        return text.lower() == "刪除課程"
    def is_going_to_delete_cource_time(self, event):
        text = event.message.text
        return text.lower() == "刪除星期幾的課程呢?"
    
    # test
    def is_going_to_test(self, event):
        text = event.message.text
        return text.lower() == "考試"
    def is_going_to_add_test(self, event):
        text = event.message.text
        return text.lower() == "增加考試"
    def is_going_to_add_test_day(self, event):
        text = event.message.text
        return text.lower() == "增加星期幾的考試?"
    def is_going_to_add_test_item(self, event):
        text = event.message.text
        return text.lower() == "增加甚麼考試"
    
    def is_going_to_search_test(self, event):
        text = event.message.text
        return text.lower() == "查詢考試"
    def is_going_to_search_test_time(self, event):
        text = event.message.text
        return text.lower() == "查詢星期幾的考試呢?"
    
    def is_going_to_delete_test(self, event):
        text = event.message.text
        return text.lower() == "刪除考試"
    def is_going_to_delete_test_time(self, event):
        text = event.message.text
        return text.lower() == "刪除星期幾的考試呢?"
    
    # homework
    def is_going_to_homework(self, event):
        text = event.message.text
        return text.lower() == "課程"
    def is_going_to_add_homework(self, event):
        text = event.message.text
        return text.lower() == "增加功課"
    def is_going_to_add_homework_day(self, event):
        text = event.message.text
        return text.lower() == "增加星期幾的功課?"
    def is_going_to_add_homework_item(self, event):
        text = event.message.text
        return text.lower() == "增加甚麼功課"
    
    def is_going_to_search_homework(self, event):
        text = event.message.text
        return text.lower() == "查詢功課"
    def is_going_to_search_homework_time(self, event):
        text = event.message.text
        return text.lower() == "查詢星期幾的功課呢?"
    
    def is_going_to_delete_homework(self, event):
        text = event.message.text
        return text.lower() == "刪除功課"
    def is_going_to_delete_homework_time(self, event):
        text = event.message.text
        return text.lower() == "刪除星期幾的功課呢?"

    #enter
    
    def on_enter_course(self, event):
        print("I'm entering course")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger course")
        self.go_back()

    def on_enter_test(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_test(self):
        print("Leaving state2")
        
    # homework
    
    def on_enter_homework(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_homework(self):
        print("Leaving state2")
        
    # 
