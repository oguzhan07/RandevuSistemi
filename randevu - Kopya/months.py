year = {
    "ocak": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    "şubat": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    "mart": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    "nisan": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    "mayıs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    "haziran": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    "temmuz": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    "ağustos": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    "eylül": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    "ekim": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    "kasım": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    "aralık": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
}






word_of_future_day = week[index_of_future] #pazartesi, salı, çarşamba...
                if word_of_future_day == "pazartesi":
                    self.num_label = QLabel(self.number_of_day)

                elif word_of_future_day == "salı":
                    self.num_label = QLabel(self.number_of_day)

                elif word_of_future_day == "çarşamba":
                    self.number_of_day -= 2
                    self.num_label = QLabel(self.number_of_day)

                elif word_of_future_day == "perşembe":
                    self.number_of_day -= 3
                    self.num_label = QLabel(self.number_of_day)

                elif word_of_future_day == "cuma":
                    self.number_of_day -= 4
                    self.num_label = QLabel(self.number_of_day)

                elif word_of_future_day == "cumartesi":
                    self.number_of_day -= 5
                    self.num_label = QLabel(self.number_of_day)

                elif word_of_future_day == "pazar":
                    self.number_of_day -= 6
                    self.num_label = QLabel(self.number_of_day)


                self.number_of_day += 1
                self.num_label.setParent(self.num_background)
                self.num_label.setGeometry(20, 5, 50, 60)
                self.num_label.setFont(oswald)


            self.num_label.raise_()

# print(today.month)
# print(today.day)
# TODAY.DAY: bugünün ayın kaçıncı günü olduğu söylüyor. for ex: "26"



        self.number_of_day = today.day