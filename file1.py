import streamlit as st

def main():
    st.set_page_config(page_title="E-commerce Application", layout="wide")

    # Define product catalog (can be connected to a database in real-world applications)
    products = [
        {"id": 1, "name": "Laptop", "price": 799.99, "image": "https://via.placeholder.com/150"},
        {"id": 2, "name": "Smartphone", "price": 499.99, "image": "https://via.placeholder.com/150"},
        {"id": 3, "name": "Headphones", "price": 99.99, "image": "https://via.placeholder.com/150"},
        {"id": 4, "name": "Smartwatch", "price": 199.99, "image": "https://via.placeholder.com/150"},
    ]

    # Session state for cart
    if "cart" not in st.session_state:
        st.session_state["cart"] = []

    # Header
    st.title("Online E-commerce Application")

    # Product browsing section
    st.subheader("Available Products")
    cols = st.columns(4)
    for i, product in enumerate(products):
        with cols[i % 4]:
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

if __name__ == "__main__":
    main()

