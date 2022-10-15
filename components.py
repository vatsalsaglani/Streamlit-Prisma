import streamlit as st
def card(title, image, overview):

    return f"""
    <div class="col">
        <div class="card" style="width: 18rem;margin-top:2px">
            <img class="card-img-top" src="https://image.tmdb.org/t/p/original{image}" alt="Card image cap">
            <div class="card-body text-dark">
                <h5 class="card-title text-dark">{title}</h5>
            </div>
        </div>
    </div>
    """


def rows(strings):
    return f"""
    <div class="row" >
        {strings}
    </div>
    """


def grid(movies):

    card_strings = [
        card(title=movie.get("meta")[0].get("title"),
             image=movie.get("meta")[0].get("poster"),
             overview=movie.get("meta")[0].get("overview")) for movie in movies if movie.get("meta")[0].get("poster")
    ]
    row_strings = "\n".join([
        rows("\n".join(card_strings[ix:ix + 4]))
        for ix in range(0, len(card_strings), 4)
    ])

    return f"""
    <div class="container" >
        {row_strings}
    </div>
    """