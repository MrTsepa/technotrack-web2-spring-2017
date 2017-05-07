export const OWNER = {
    name: 'Stas',
    avaSrc: '',
};

export const POST = {
    id: 0,
    owner: OWNER,
    title: 'Lorem ipsum',
    time: '19 Feb at 12:01 p',
    content: 'Lorem ipsum dolor sit amet, nibh volutpat tincidunt, risus nec laborum maecenas a lectus, ullamcorper nunc congue ligula neque tempor magnis, proin integer vel tincidunt ante. Nulla velit nisl quisque netus. Nunc penatibus cras lobortis etiam, ipsum ut elit in ante fusce curabitur, fermentum sed sed ipsum. Nibh cursus, est molestie nunc quia, faucibus massa ante dolor integer, volutpat turpis, sit nisl purus. Fringilla pede porta, urna risus arcu sunt nulla, nec tortor, in dolor dui curabitur vitae, eleifend neque neque dolor.',
    likescount: 200,
};

export const POSTS = {
    0: { ...POST, id: 0 },
    1: { ...POST, id: 1 },
    2: { ...POST, id: 2 },
    3: { ...POST, id: 3 },
    4: { ...POST, id: 4 },
    5: { ...POST, id: 5 },
    6: { ...POST, id: 6 },
};

export const POST_RESPONCE = {
    postList: [1, 3, 5],
    posts: POSTS,
};
