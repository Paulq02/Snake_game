"""def compare_score(self):
           for score in self.top_score_list:
                if score > self.high_score:
                    self.high_score = score

                    

    def write_score(self):
        with open("data.txt", mode="w") as f_handle:
            f_handle.write(str(self.high_score))
        
        with open("data.txt", mode="w") as f_handle:
                f_handle.write(str(self.high_score))


    def read_txt_score(self):
        with open("data.txt") as f_handle:
            content = f_handle.read()
            converted_content = int(content)
            self.top_score_list.append(converted_content)
            """
