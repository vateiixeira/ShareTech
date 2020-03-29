var productList = new Vue({
    el:'#product-list',
    data:{
      message : 'Hello',
      shopbymenu: true,
      productItemsNumbers: 19,
      filtertoApply:['size'],
      filtersAppied: [],
      genders: ['male', 'female'],
      colors: ['red','blue','black', 'white', 'gold'],
      materials:['leather','recycled cork','microfiber','mesh','wool','canvas','knit','Rubber'],
      sizes:[7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 12, 12.5, 13, 14],
      colorsActive: [],
      sizesActive: [],
      filteredItems2:[],
  
  
      products:[
        {
          id: 1,
          name: 'Shoes Male Only Pair',
          price: 5,
          gender: ['male'],
          description: 'Bold & solid.',
          category: 'shoes',
          tag: '',
          image: 'http://via.placeholder.com/350x350',
          size: [7,7.5, 8],
          color:['red','blue','black']
        },
        {
          id: 2,
          name: 'Footbed Thin',
          price: 1,
          gender: ['male','female'],
          description: 'Bold & solid.fdff',
          category: 'footbed',
          tag: 'dddddd',
          image: 'http://via.placeholder.com/350x350',
          size: [7,7.5, 8],
          color:['blue']
        },
        {
          id: 3,
          name: 'The Square 3434Pair',
          price: 99,
          gender: ['male','female'],
          description: 'Bold & solid.fdff',
          category: 'footbed',
          tag: 'dddddd',
          image: 'http://via.placeholder.com/350x350',
          size: [7,7.5, 8],
          color:['blue', 'red']
        },
        {
          id: 4,
          name: 'The Square 3434Pair',
          price: 99,
          gender: ['male','female'],
          description: 'Bold & solid.fdff',
          category: 'footbed',
          tag: 'dddddd',
          image: '[% settings.media_url %]/images/place-holder.jpg',
          size: [14],
          color:['blue']
        },
        {
          id: 5,
          name: 'No color ',
          price: 999,
          gender: ['male','female'],
          description: 'Bold & solid.fdff',
          category: 'footbed',
          tag: 'dddddd',
          image: '[% settings.media_url %]/images/place-holder.jpg',
          size: [14],
          color:[ ]
        },
        {
          id: 6,
          name: 'The Square 3434Pair',
          price: 1,
          gender: ['male','female'],
          description: 'Bold & solid.fdff',
          category: 'footbed',
          tag: 'dddddd',
          image: '[% settings.media_url %]/images/place-holder.jpg',
          size: [10],
          color:['blue']
        },
        {
          id: 7,
          name: 'The Square 3434Pair',
          price: 1,
          gender: ['male','female'],
          description: 'Bold & solid.fdff',
          category: 'footbed',
          tag: 'dddddd',
          image: '[% settings.media_url %]/images/place-holder.jpg',
          size: [10],
          color:['blue']
        },
        {
          id: 8,
          name: 'The Square 3434Pair',
          price: 1,
          gender: ['male','female'],
          description: 'Bold & solid.fdff',
          category: 'footbed',
          tag: 'dddddd',
          image: 'http://via.placeholder.com/350x350',
          size: [10],
          color:['red']
        },
        {
          id: 9,
          name: 'The Square 3434Pair',
          price: 1,
          gender: ['male','female'],
          description: 'Bold & solid.fdff',
          category: 'footbed',
          tag: 'dddddd',
          image: '[% settings.media_url %]/images/place-holder.jpg',
          size: [10],
          color:['blue']
        }
  
      ],
    },
    computed: {
      filteredItems: function() {
        return this.products.filter( product => {
          return this.filtersAppied.every( filterAppied => {
            if (product.color.includes(filterAppied)) {
              return product.color.includes(filterAppied);
            }
            if (product.size.includes(filterAppied)) {
              return product.size.includes(filterAppied);
            }
          });
        });
      },
  
      sortByLowPrice: function() {
        return this.products.sort(function(a,b) {
           return a.price - b.price ;
        })
      },
      sortByHigherPrice: function() {
        return this.products.sort(function(a,b) {
           return a.price - b.price ;
        })
      }
  
    },
  
    methods:{
   
      removeTags : function (item) {
        this.filtersAppied.pop(item)
      },
  
      setActive: function(element){
        if(this.filtersAppied.indexOf(element) > -1){
          this.filtersAppied.pop(element)
        }else{
          this.filtersAppied.push(element)
        }
      },
      isActive: function (menuItem) {
        return this.filtersAppied.indexOf(menuItem) > -1
      },
  
    }
  });
     
      console.log(productList.filteredItems);
    
    $( document ).ready(function() {
    
  
       // Product grid
       const gridItem= $('.grid-item-wrapper');
  
       gridItem.on('mouseenter', function(){
         $(this).addClass('active');
       })
      //  console.log('rererer');
  
       gridItem.on('mouseleave', function(){
         $(this).removeClass('active');
       })
  
    })