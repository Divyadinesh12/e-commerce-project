class WebLocator:
    """
    this class contains all the locators that are required to testing add to cart button
    """
    def __init__(self):
        self.phone_button_locator = "//a[normalize-space()='Phones & PDAs']"
        self.iphone_locator = "//a[normalize-space()='iPhone']"
        self.first_pic_locator = " //li[1]//a[1]//img[1]"
        self.all_photo_left_button = "//button[@title='Next (Right arrow key)']"
        self.x_button_locator="//button[normalize-space()='×']"
        self.quantity_locator="//input[@id='input-quantity']"
        self.add_to_cart_button="//button[@id='button-cart']"
        self.success_message_phone_locator="//div[@class='alert alert-success alert-dismissible']"
        self.cart_button="//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']"
        self.cart_right_text_button = "//td[@class='text-right']"
        self.laptop_locator="//a[normalize-space()='Laptops & Notebooks']"
        self.all_laptop_locator="//a[normalize-space()='Show AllLaptops & Notebooks']"
        self.specific_model_locator="//a[normalize-space()='HP LP3065']"
        self.add_to_cart_laptop="//button[@id='button-cart']"
        self.calendar_locator="//i[@class='fa fa-calendar']"
        self.backward_button_locator="//th[@class='next']"
        self.month_year_locator="//th[normalize-space()='April 2011']"
        self.date_locator="//td[normalize-space()='16']"
