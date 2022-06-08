<template lang="">
  <div class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
    <div class="card mb-3" v-for="cart in carts" :key="cart.id">
      
      <div class="card-content">
        <div class="media">
          <div class="media-content text-center">
            <p class="title is-5">Cart №{{ cart.id }} from: {{ formatDate(cart.date) }} Manager: 
              <span v-if="cart.user.is_staff" class="text-success">{{ cart.user.username }}</span>
              <span v-else class="text-secondary">{{ cart.user.username }}</span>
            </p>
          </div>
        </div>
        <OrderList :cartId="cart.id"></OrderList>
        <div class="d-flex justify-content-between">
          <div class="ml-auto">
            <i title="Add product" @click="addProduct(cart.id)" class="bi bi-file-plus me-3 text-info"></i>
            <i @click="checkout(cart.id)" class="bi bi-cart-check me-3 text-success"></i>
            <router-link :to="{ name: 'cartDelete', params: { id: cart.id } }">
              <i class="bi bi-cart-x me-3 text-danger"></i>
            </router-link>

          </div>
          
        </div>
      </div>
      
        
      
    </div>
    <div class="d-flex justify-content-center">
      <router-link title="Add new cart" :to="{ name: 'cartAdd' }" class="btn btn-primary text-center mt-5"><i class="bi bi-cart-plus"></i></router-link>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import OrderList from '../order/OrderList.vue';
export default {
  components: {
    OrderList
  },
  data() {
    return {
      carts: [],
    }
  },
  methods: {
    async getOrders() {
      await axios.get('/carts/')
        .then(response => {
          this.carts = response.data;
        })
        .catch(error => {
          console.log(error)
        })
    },
      formatDate(date) {
      return new Date(date).toLocaleString(undefined, {year: 'numeric', month: '2-digit', day: '2-digit', weekday:"long", hour: '2-digit', hour12: false, minute:'2-digit', second:'2-digit'});
      },
    async checkout(id) {
      confirm('Are you sure you want to checkout this cart?');
    },
    async addProduct(id) {
      this.$router.push({ name: 'order-product', params: { id: id } });
    },
  },
  mounted() {
    this.getOrders();
  },
  
}
</script>
<style lang="">
  
</style>