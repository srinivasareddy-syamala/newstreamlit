import streamlit as st

def login():
    """Login mechanism."""
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "admin" and password == "password":  # Replace with secure auth in real apps
                st.session_state["logged_in"] = True
                st.success("Login successful!")
                display_products()
            else:
                st.error("Invalid username or password")
        return False
    return True

def display_products():
    """Display the product catalog."""
    # Define product catalog (can be connected to a database in real-world applications)
    products = [
        {"id": 1, "name": "Laptop", "price": 799.99, "image": "laptop.jpg"},
        {"id": 2, "name": "Smartphone", "price": 499.99, "image": "smartphone.jpg"},
        {"id": 3, "name": "Headphones", "price": 99.99, "image": "headphones.jpg"},
        {"id": 4, "name": "Smartwatch", "price": 199.99, "image": "smartwatch.jpg"},
    ]

    # Session state for cart
    if "cart" not in st.session_state:
        st.session_state["cart"] = []

    # Header
    st.title("Online E-commerce Application")

    # Product browsing section
    st.subheader("Available Products")
    cols = st.columns(len(products))  # Use the exact number of columns as products
    for i, product in enumerate(products):
        with cols[i]:
            st.image(product["image"], caption=product["name"], use_column_width=True)
            st.write(f"**Price:** ${product['price']:.2f}")
            if st.button(f"Add to Cart - {product['name']}", key=f"add_{product['id']}"):
                st.session_state["cart"].append(product)
                st.success(f"{product['name']} added to cart!")

    # Cart section
    st.subheader("Your Cart")
    if st.session_state["cart"]:
        cart_items = st.session_state["cart"]
        total_cost = sum(item['price'] for item in cart_items)

        for item in cart_items:
            st.write(f"- **{item['name']}**: ${item['price']:.2f}")

        st.write(f"**Total Cost:** ${total_cost:.2f}")

        if st.button("Clear Cart"):
            st.session_state["cart"] = []
            st.success("Cart cleared!")

        if st.button("Checkout"):
            st.success("Thank you for your purchase!")
            st.session_state["cart"] = []
    else:
        st.write("Your cart is empty.")

def main():
    st.set_page_config(page_title="E-commerce Application", layout="wide")

    if login():
        display_products()

if __name__ == "__main__":
    main()

