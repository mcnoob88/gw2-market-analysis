import pickle
import streamlit as st 


#app=Flask(__name__)
#Swagger(app)

pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(quantity):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
        -   name: quantity
            in: query
            type: number
            required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=model.predict([[quantity]])
    print(prediction)
    return prediction



def main():
    st.title("Deldrimor Price Predicttion")

    quantity = st.text_input("Quantity","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(quantity)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("This is a simple app for deldrimor price prediction.")

if __name__=='__main__':
    main()