# encoding: utf-8
__author__ = 'scheuing'

class CVDate:
    number_post = {0:'', 1:'1st', 2:'2nd', 3:'3rd'}
    month_en = {0:'', 1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    month_de = {0:'', 1:'Januar', 2:'Februar', 3:'März', 4:'April', 5:'Mai', 6:'Juni', 7:'Juli', 8:'August', 9:'September', 10:'Oktober', 11:'November', 12:'Dezember'}
    month_short_en={0:'',1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    month_short_de={0:'',1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Okt', 11:'Nov', 12:'Dez'}

    def __init__(self, year, month=0, day=0):
        self.year=year
        self.month=month
        self.day=day

    def format(self, form, language):
        """

        :param form: str representing the format of the date string.
        For numbers use: year: {y:}, month: {m:}, day: {d:}
        For written names (1st, November) use: month {MM:} (e.g. Novenber) {M:} (e.g. Nov), day:{D:}
        :return: string representation of self
        """

        if language == 'en':
            month = self.month_en
            month_short = self.month_short_en
            D = str(self.day)+self.number_post[self.day] if self.day in self.number_post.keys() else str(self.day)+'th'
        elif language == 'de':
            month = self.month_de
            month_short = self.month_short_de
            D = str(self.day)+'tem'
        else:
            month = self.month_en
            month_short = self.month_short_en
            D = self.number_post[self.day] if self.day in self.number_post.keys() else 'th'

        M = month_short[self.month]
        MM = month[self.month]
        ret = form.format(M=M, MM=MM, D=D, y=self.year, m=self.month, d=self.day)
        return ret

