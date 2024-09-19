from flask import Flask, redirect, url_for, render_template, request, jsonify
from web_to_csv import get_matches, s_year, add_to_csv, find_present_substring, get_dates, add_to_csv_2021
from getmatch import get_winners, s_myear
from c_table import get_table, get_ptable, get_date_from_to, get_rem,convert_dict_to_list,convert_list_to_dict
from updatetable import nextmatch_update
import json

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/demotest")
def demotest():
    return render_template('demo.html')


@app.route('/demotest/get_content', methods=['POST'])
def get_content():
    selected_option = ""
    selected_option = request.form.get('option')
    selected_date = request.form.get('date')
    # Perform your calculations here based on the selected_option
    if selected_option:
        year = int(selected_option)
        if year == 2021:
            add_to_csv_2021()
            result = get_table()
            date_list = get_date_from_to()
            return jsonify({'result': result, 'dates': date_list})
        else:
            mlink = s_myear(year)
            link = s_year(year)
            dates = get_dates(link)
            winners = get_winners(mlink)
            matches = get_matches(link)
            add_to_csv("data.csv", matches, dates, winners)
            result = get_table()
            date_list = get_date_from_to()
            return jsonify({'result': result, 'dates': date_list})
    # get corressponding main.py for demo.html
    # selected_date = request.form.get('date')
    # Print the selected date to the terminal

    if selected_date:
        try:
            cur_result, cur_result2 = get_ptable(selected_date)
            rem_matches = get_rem(selected_date)
            # Handle the date logic here. For demonstration, we just return the selected date.
            # Replace with your actual logic.
            return jsonify({'cur_result': cur_result, 'rem_matches': rem_matches})

            # return jsonify({'message': f'Selected date: {selected_date}'}), 200

        except Exception as e:
            # Return an error response if something goes wrong
            return jsonify({'error': str(e)}), 500
    return "Date received and printed to terminal."


@app.route("/newpage")
def newpage():
    selected_date = request.args.get('selected_date')
    return render_template('update.html', selected_date=selected_date)


@app.route('/newpage/get_updates', methods=['GET'])
def get_updates():
    selected_date = request.args.get('selected_date')
    cur_result, cur_result2 = get_ptable(selected_date)
    cur_result2_2=convert_dict_to_list(cur_result2)
    rem_matches = get_rem(selected_date)
    return jsonify({'cur_result': cur_result, 'cur_result2_2': cur_result2_2, 'rem_matches': rem_matches})


@app.route('/newpage/get_updates/submit_data', methods=['POST'])
def submit_data():
    # matchindex=0
    output_radio=int(request.form.get('output_radio'))
    matchindex=int(request.form.get('matchindex'))
    first_bat = request.form.get('first_bat')
    second_bat = request.form.get('second_bat')
    score1 = int(request.form.get('score1'))
    score2 = int(request.form.get('score2'))
    overs1 = float(request.form.get('overs1'))
    overs2 = float(request.form.get('overs2'))
    cur_result2_2 = request.form.get('cur_result2_2')
    selected_date=request.form.get('date_selected')
    print(output_radio,"          ",matchindex,"              ",first_bat,"               ",second_bat)
    print("\n","          ",score1,"           ",score2,"             ",overs1,"           ",overs2,"            ")








    
    # rem=request.form.get('rem_matches')
    # first_bat = request.form.get('first_bat')
    # second_bat = request.form.get('second_bat')
    # score1 = request.form.get('score1')
    # score2 = request.form.get('score2')
    # overs1 = request.form.get('overs1')
    # overs2 = request.form.get('overs2')
    # cur_result2_2 = request.form.get('cur_result2_2')
    print("hi")
    print("hello")
    cur_result2_2_serialized = request.form.get('cur_result2_2')

    # Deserialize the JSON string into a Python list of lists
    cur_result2_2 = json.loads(cur_result2_2_serialized)
    print(cur_result2_2)
    dict_cur_result2_2=convert_list_to_dict(cur_result2_2)
    print("kkkkkkkkkkkkkkkk\nkkkkkkkkkkkkkkkkkkkkkkk")
    print(dict_cur_result2_2)
    print("kkkkkkkkkkkkkkkk\nkkkkkkkkkkkkkkkkkkkkkkk")
    cur_result, cur_result2 = nextmatch_update(first_bat,output_radio,dict_cur_result2_2, first_bat, second_bat, score1, score2, overs2)
    
    matchindex+=1
    for i in range(len(cur_result[0])):
        print(cur_result[0][i], "\t\t", cur_result[1][i], "\t", cur_result[2][i],
            "\t", cur_result[3][i], "\t", cur_result[4][i], "\t", cur_result[5][i], "\t")
    rem_matches = get_rem(selected_date)

    cur_result2_2=convert_dict_to_list(cur_result2)

    return jsonify({'win':first_bat,'first_bat':first_bat,'second_bat':second_bat,'score1':score1,'score2':score2,'overs1':overs1,'overs2':overs2,'cur_result': cur_result, 'cur_result2_2': cur_result2_2, 'rem_matches': rem_matches,'matchindex':matchindex})

    # return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/get_content', methods=['POST'])
# def get_content():
#     selected_option = request.form.get('option')
#     # Perform your calculations here based on the selected_option
#     if selected_option == 'option1':
#         result = ['Item 1.1', 'Item 1.2', 'Item 1.3']
#     elif selected_option == 'option2':
#         result = ['Item 2.1', 'Item 2.2', 'Item 2.3']
#     elif selected_option == 'option3':
#         result = ['Item 3.1', 'Item 3.2', 'Item 3.3']
#     else:
#         result = []
#     return jsonify(result)


# if __name__ == '__main__':
#     app.run(debug=True)
