export const initialData = {
  selected: 'casa-di-pasta', favorites: [],
  restaurants: [
    { id:'casa-di-pasta', name:'Casa di Pasta', cuisine:'Italiana', description:'Massas artesanais, receitas de família e tempo para saborear.', cover:'/assets/casa.jpg', hours:'Seg a sáb · 11h às 22h', address:'Vila dos Sabores · Local de demonstração', color:'#B84E29', categories:['Entradas','Pratos principais','Bebidas','Sobremesas'] },
    { id:'verde-grao', name:'Verde & Grão', cuisine:'Saudável', description:'Comida leve, ingredientes frescos e escolhas que fazem bem.', cover:'/assets/verde.jpg', hours:'Seg a sex · 10h às 19h', address:'Praça do Campus · Local de demonstração', color:'#4F7A4E', categories:['Pratos','Bebidas'] },
    { id:'brasa-urbana', name:'Brasa Urbana', cuisine:'Brasileira', description:'O sabor da brasa e o carinho da comida brasileira.', cover:'/assets/brasa.jpg', hours:'Ter a dom · 11h às 23h', address:'Rua dos Sabores · Local de demonstração', color:'#B84E29', categories:['Pratos','Bebidas'] }
  ],
  products:[
    {id:'p1',restaurant:'casa-di-pasta',name:'Bruschetta da casa',description:'Pão rústico tostado, tomates frescos, manjericão e azeite extravirgem. 4 unidades.',price:24.9,category:'Entradas',photo:'/assets/bruschetta.jpg',available:true},
    {id:'p2',restaurant:'casa-di-pasta',name:'Arancini de queijo',description:'Bolinhos de risoto recheados com queijo, crocantes por fora. Acompanha molho de tomate.',price:29.9,category:'Entradas',photo:'/assets/arancini.jpg',available:true},
    {id:'p3',restaurant:'casa-di-pasta',name:'Spaghetti alla carbonara',description:'Massa artesanal com guanciale, pecorino, gemas e pimenta-do-reino. Receita italiana clássica.',price:49.9,category:'Pratos principais',photo:'/assets/carbonara.jpg',available:true},
    {id:'p4',restaurant:'casa-di-pasta',name:'Lasanha à bolonhesa',description:'Camadas de massa fresca, ragù de carne, béchamel e parmesão gratinado.',price:46.9,category:'Pratos principais',photo:'/assets/lasanha.jpg',available:true},
    {id:'p5',restaurant:'casa-di-pasta',name:'Lasanha para compartilhar',description:'Nossa lasanha à bolonhesa em uma porção especial para duas pessoas.',price:79.9,category:'Pratos principais',photo:'/assets/lasanha.jpg',available:false},
    {id:'p6',restaurant:'casa-di-pasta',name:'Água mineral',description:'Água mineral sem gás, garrafa de 500 ml.',price:6,category:'Bebidas',photo:'',available:true},
    {id:'p7',restaurant:'casa-di-pasta',name:'Limonada da casa',description:'Limão fresco, água filtrada e hortelã. Copo de 350 ml.',price:12,category:'Bebidas',photo:'',available:true},
    {id:'p8',restaurant:'casa-di-pasta',name:'Café espresso',description:'Café de torra média, preparado na hora. Xícara de 50 ml.',price:7,category:'Bebidas',photo:'',available:true},
    {id:'p9',restaurant:'casa-di-pasta',name:'Panna cotta',description:'Creme italiano de baunilha com calda de frutas vermelhas.',price:19.9,category:'Sobremesas',photo:'',available:true},
    {id:'p10',restaurant:'casa-di-pasta',name:'Tiramisù',description:'Camadas de mascarpone, biscoitos embebidos em café e cacau.',price:22.9,category:'Sobremesas',photo:'',available:false},
    {id:'v1',restaurant:'verde-grao',name:'Bowl do dia',description:'Arroz integral, legumes assados, folhas frescas e molho de ervas.',price:32.9,category:'Pratos',photo:'',available:true},
    {id:'v2',restaurant:'verde-grao',name:'Suco verde',description:'Couve, maçã, limão e gengibre. 350 ml.',price:14,category:'Bebidas',photo:'',available:true},
    {id:'b1',restaurant:'brasa-urbana',name:'Prato da brasa',description:'Carne na brasa, arroz, feijão, farofa e vinagrete.',price:39.9,category:'Pratos',photo:'',available:true},
    {id:'b2',restaurant:'brasa-urbana',name:'Suco de laranja',description:'Laranjas espremidas na hora. Copo de 350 ml.',price:12,category:'Bebidas',photo:'',available:true}
  ]
};
