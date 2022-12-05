from transitions import Machine
from linebot.models import *
from utils import send_text_message
from utils import send_text_message, send_button_message
# import json
course = [[],[],[],[],[],[],[]]
global date
class TocMachine(Machine):
    def __init__(self, **machine_configs):
        self.machine = Machine(model=self, **machine_configs)
    
    def is_going_to_Start(self, event):
        return True
    def on_enter_start(self, event):
        print("I'm entering start")
        send_button_message(
            reply_token = event.reply_token,
            title='請問需要做甚麼',
            text='請選擇課程/考試/功課',
            action = [
                MessageTemplateAction(label = '課程',text = '課程'),
                MessageTemplateAction(label = '考試',text = '考試'),
                MessageTemplateAction(label = '功課',text = '功課'),
            ]
        )
    # course
    def is_going_to_course(self, event):
        text = event.message.text
        return text.lower() == "課程"
    
    def on_enter_course(self,event):
        print("I'm entering course")
        send_button_message(
            reply_token = event.reply_token,
            title='課程功能',
            text='請選擇以下功能',
            action = [
                MessageTemplateAction(label = '增加課程',text = '增加課程'),
                MessageTemplateAction(label = '查詢課程',text = '查詢課程'),
                MessageTemplateAction(label = '刪除課程',text = '刪除課程')
            ]
        )
    def is_going_to_return(self,event):
        return True
    # add course
    def is_going_to_add_course(self, event):
        text = event.message.text
        return text.lower() == "增加課程"
    
    def on_enter_add_course(self,event):
        send_text_message(event.reply_token,"請輸入星期幾(1~7)")
            
    def is_going_to_add_course_day(self, event):
        text = event.message.text
        if text.lower().isnumeric() and date in range(1,8):
            date = int(text)
            return True
        return False
    
    def on_enter_add_course_day(self,event):
        send_text_message(event.reply_token,"請輸入想增加的考試項目")
        
    def is_going_to_add_course_item(self, event):
        text = event.message.text
        course[date].append(text)
        return True
    
    # search course
    def is_going_to_search_course(self, event):
        text = event.message.text
        return text.lower() == "查詢課程"
    
    def on_enter_search_course(self,event):
        send_text_message(event.reply_token,"請輸入星期幾(1~7)")
            
    def is_going_to_search_course_day(self, event):
        text = event.message.text
        if text.lower().isnumeric() and date in range(1,8):
            date = int(text)
            return True
        return False
    
    def on_enter_search_course_day(self,event):
        send_text_message(event.reply_token,course[date])
        
    # delete course
    def is_going_to_delete_course(self, event):
        text = event.message.text
        return text.lower() == "刪除課程"
    
    def on_enter_delete_course(self,event):
        send_text_message(event.reply_token,"請輸入星期幾(1~7)")
            
    def is_going_to_delete_course_day(self, event):
        text = event.message.text
        if text.lower().isnumeric() and date in range(1,8):
            date = int(text)
            return True
        return False
    
    def on_enter_delete_course_day(self,event):
        course[date].clear
    
    # # test
    # def is_going_to_test(self, event):
    #     text = event.message.text
    #     return text.lower() == "考試"
    # def is_going_to_add_test(self, event):
    #     text = event.message.text
    #     return text.lower() == "增加考試"
    # def is_going_to_add_test_day(self, event):
    #     text = event.message.text
    #     return text.lower() == "增加星期幾的考試?"
    # def is_going_to_add_test_item(self, event):
    #     text = event.message.text
    #     return text.lower() == "增加甚麼考試"
    
    # def is_going_to_search_test(self, event):
    #     text = event.message.text
    #     return text.lower() == "查詢考試"
    # def is_going_to_search_test_time(self, event):
    #     text = event.message.text
    #     return text.lower() == "查詢星期幾的考試呢?"
    
    # def is_going_to_delete_test(self, event):
    #     text = event.message.text
    #     return text.lower() == "刪除考試"
    # def is_going_to_delete_test_time(self, event):
    #     text = event.message.text
    #     return text.lower() == "刪除星期幾的考試呢?"
    
    # # homework
    # def is_going_to_homework(self, event):
    #     text = event.message.text
    #     return text.lower() == "功課"
    # def is_going_to_add_homework(self, event):
    #     text = event.message.text
    #     return text.lower() == "增加功課"
    # def is_going_to_add_homework_day(self, event):
    #     text = event.message.text
    #     return text.lower() == "增加星期幾的功課?"
    # def is_going_to_add_homework_item(self, event):
    #     text = event.message.text
    #     return text.lower() == "增加甚麼功課"
    
    # def is_going_to_search_homework(self, event):
    #     text = event.message.text
    #     return text.lower() == "查詢功課"
    # def is_going_to_search_homework_time(self, event):
    #     text = event.message.text
    #     return text.lower() == "查詢星期幾的功課呢?"
    
    # def is_going_to_delete_homework(self, event):
    #     text = event.message.text
    #     return text.lower() == "刪除功課"
    # def is_going_to_delete_homework_time(self, event):
    #     text = event.message.text
    #     return text.lower() == "刪除星期幾的功課呢?"

    # #enter
    
    
    # def on_enter_test(self,event):
    #     print("I'm entering course")
    #     send_button_message(
    #         reply_token = event.reply_token,
    #         title='考試功能',
    #         text='請選擇以下功能',
    #         action = [
    #             MessageTemplateAction(label = '增加考試',text = '增加考試'),
    #             MessageTemplateAction(label = '查詢考試',text = '查詢考試'),
    #             MessageTemplateAction(label = '刪除考試',text = '刪除考試'),
    #         ]
    #     )
    # def on_enter_homework(self,event):
    #     print("I'm entering course")
    #     send_button_message(
    #         reply_token = event.reply_token,
    #         title='課程功課',
    #         text='請選擇以下功能',
    #         action = [
    #             MessageTemplateAction(label = '增加功課',text = '增加功課'),
    #             MessageTemplateAction(label = '查詢功課',text = '查詢功課'),
    #             MessageTemplateAction(label = '刪除功課',text = '刪除功課'),
    #         ]
    #     )

    
        
    # # homework
    
    # def on_enter_homework(self, event):
    #     print("I'm entering state2")

    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Trigger state2")
    #     self.go_back()

    # def on_exit_homework(self):
    #     print("Leaving state2")
        
    # # 
