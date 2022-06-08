import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue'
import axios from 'axios';


import HomePage from '@/components/main/HomePage.vue';

import CategoryList from '@/components/category/CategoryList.vue';
import CategoryDetail from '@/components/category/CategoryDetail.vue';
import CategoryEdit from '@/components/category/CategoryEdit.vue';
import CategoryDelete from '@/components/category/CategoryDelete.vue';

import ProductList from '@/components/product/ProductList.vue';
import ProductAdd from '@/components/product/ProductAdd.vue';
import ProductDelete from '@/components/product/ProductDelete.vue';
import ProductDetail from '@/components/product/ProductDetail.vue';
import ProductEdit from '@/components/product/ProductEdit.vue';

import OrderList from '@/components/order/OrderList.vue';
import OrderDetail from '@/components/order/OrderDetail.vue';
import OrderProduct from '@/components/order/OrderProduct.vue';

import CartList from '@/components/cart/CartList.vue';
import CartDetail from '@/components/cart/CartDetail.vue';
import CartAdd from '@/components/cart/CartAdd.vue';
import CartDelete from '@/components/cart/CartDelete.vue';

axios.defaults.baseURL = 'http://localhost:8000/api/v1/';


const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'home', component: HomePage },

    { path: '/categories', name: 'categories', component: CategoryList },
    { path: '/categoryedit/:id', name:'categoryEdit', component: CategoryEdit, props: true },
    { path: '/categorydelete', name:'categoryDelete', component: CategoryDelete, props: true },
    { path: '/categorydetail', name: 'categoryDetail', component: CategoryDetail, props: true },
    
    { path: '/products', name: 'products', component: ProductList },
    { path: '/productadd/:id', name: 'productAdd', component: ProductAdd, props: true },
    { path: '/productedit/:id', name: 'productEdit', component: ProductEdit, props: true },
    { path: '/productdelete', name: 'productDelete', component: ProductDelete, props: true },
    { path: '/productdetail', name: 'productDetail', component: ProductDetail, props: true },

    { path: '/orders', name: 'orders', component: OrderList },
    { path: '/order/:cart_id', name: 'orderDetail', component: OrderDetail, props: true },

    { path: '/carts', name: 'carts', component: CartList, props: true },
    { path: '/cart/:id', name: 'cartDetail', component: CartDetail, props: true },
    { path: '/cartadd', name: 'cartAdd', component: CartAdd },
    { path: '/cartdelete', name: 'cartDelete', component: CartDelete, props: true },

    { path: '/product-to-order', name: 'order-product', component: OrderProduct, props: true },
  ]
});

createApp(App)
.use(router, axios)
.mount('#app')
