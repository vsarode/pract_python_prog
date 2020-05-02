import re, os, glob, collections


class CarbonUILog:
    def _init_(self):
        pass

    def get_value_for_key(self, key, query_line):
        tag_index = query_line.find(key)
        while query_line[tag_index] != '=':
            tag_index += 1
        value = ""
        le = len(query_line)
        i = tag_index+2 if query_line[tag_index + 1] == "'" else tag_index + 1
        while i < le:
            if query_line[i] not in ["'", " "]:

                value += query_line[i]
            else:
                return value
            i += 1
        return value

    def fetch_tag(self, search_tags, profile_details, file_path, line_num):
        # print(search_tag, expected_vals, file_path)
        files = glob.glob(file_path)
        files.sort(key=os.path.getmtime, reverse=True)
        print("\n".join(files))
        matched_tags = []
        try:
            pattern = re.compile(list(profile_details.keys())[0]+"=")
            is_matched = False
            with open(files[0], 'r') as myfile:
                lines = myfile.readlines()
                line_index = line_num
                while line_index < len(lines):
                    line = lines[line_index]
                    result = pattern.search(line)
                    if result and not is_matched:
                        result_profile_dict = {k: self.get_value_for_key(k, line) for k, v in profile_details.items()}
                        if result_profile_dict == profile_details:
                            is_matched = True
                            print("Expected version is there in file.")
                    if is_matched:
                        for key, value in search_tags.items():
                            tag_index = line.find(key+"=")
                            if tag_index != -1:
                                tag_value = self.get_value_for_key(key, line)
                                if tag_value == value:
                                    matched_tags.append({key, value})
                        if len(matched_tags)==len(search_tags):
                            return matched_tags, line_index
                    line_index += 1
                return matched_tags, line_index
        except IOError:
            print(" Problem with file ")


if __name__ == '__main__':
    c = CarbonUILog()
    first_tag, first_line_no = c.fetch_tag({'sagar': "123", 'ram': '345'},
                                           {'Version': '123', 'Profile': 'UK', 'OwnerID': 'digvijay'},
                                           '/home/vitthals/pract/python/prog/array/input.txt', 0)
    print("res-->", first_tag, first_line_no)

    second_tag, second_line_no = c.fetch_tag({'digvijay':'321', 'ram': '899'},{'Version': '123', 'Profile': 'UK', 'OwnerID': 'digvi'},
                                             '/home/vitthals/pract/python/prog/array/input.txt', first_line_no)
    print("res--->", second_tag, second_line_no)

    line = "fasads dsadsaa  Version='123' Profile='UK' OwenerId='digvijay' dasdada dsad"
