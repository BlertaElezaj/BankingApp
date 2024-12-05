from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from base_enum import BaseEnum


class BankingAppGUI(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # List of account details
        accounts = [
            {"owner": "User1", "balance": 500.0},
            {"owner": " User2", "balance": 1000.0},
            {"owner": "User3", "balance": 1500.0}
        ]

        for account in accounts:
            owner_label = Label(text=f"Account Owner: {account['owner']}")
            balance_label = Label(text=f"Balance: ${account['balance']}")
            layout.add_widget(owner_label)
            layout.add_widget(balance_label)

            action_spinner = Spinner(text='Select Action', values=[BaseEnum.DEPOSIT, BaseEnum.WITHDRAW])
            layout.add_widget(action_spinner)

            amount_input = TextInput(hint_text='Enter Amount', input_type='number')
            layout.add_widget(amount_input)

            action_button = Button(text='Perform Action')
            action_button.bind(on_press=lambda instance, acc=account: self.perform_action(acc, balance_label, action_spinner.text, amount_input.text))
            layout.add_widget(action_button)

        return layout

    def perform_action(self, account, balance_label, action, amount):
        try:
            amount = float(amount)
            if action == BaseEnum.DEPOSIT:
                account['balance'] += amount
                balance_label.text = f"Balance: ${account['balance']}"
                popup = Popup(title='Success', content=Label(text='Deposit Successful!'), size_hint=(None, None), size=(200, 100))
            elif action == BaseEnum.WITHDRAW:
                if amount <= account['balance']:
                    account['balance'] -= amount
                    balance_label.text = f"Balance: ${account['balance']}"
                    popup = Popup(title='Success', content=Label(text='Withdrawal Successful!'), size_hint=(None, None), size=(200, 100))
                else:
                    popup = Popup(title='Error', content=Label(text='Insufficient Balance!'), size_hint=(None, None), size=(200, 100))
            else:
                popup = Popup(title='Error', content=Label(text='Invalid Action!'), size_hint=(None, None), size=(200, 100))
        except ValueError:
            popup = Popup(title='Error', content=Label(text='Invalid Amount Input!'), size_hint=(None, None), size=(200, 100))
        popup.open()


if __name__ == '__main__':
    BankingAppGUI().run()
