<template>
  <div class="container">
    <h3 class="text-center title">Edit product</h3>
    <form class="container" @submit.prevent>
      <div class="mb-3">
        <label for="inputTitle" class="form-label">Title</label>
        <input type="text" class="form-control" id="inputTitle" v-model="product.name">
        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
      </div>
      <div class="mb-3">
        <label for="inputDescription" class="form-label" >Description</label>
        <input type="textarea" class="form-control" id="inputDescription" v-model="product.description">
      </div>
      <div class="mb-3">
        <label for="inputPrice" class="form-label" >Price</label>
        <input type="number" step="0.01" class="form-control" id="inputPrice" v-model="product.price">
      </div>
      <div class="mb-3">
        <label for="inputUnit" class="form-label" >Unit</label>
        <input class="form-control" id="inputUnit" v-model="product.unit">
      </div>
      <div class="mb-3">
        <label for="inputQuantity" class="form-label" >Quantity</label>
        <input type="number" step="0.01" class="form-control" id="inputQuantity" v-model="product.quantity">
      </div>
      <div class="mb-3">
        <label for="inputBarcode" class="form-label" >Barcode</label>
        <input type="number" class="form-control" id="inputBarcode" v-model="product.barcode">
      </div>
      <div class="mb-3 form-check">
        <label for="inputIsExpired" class="form-label" >Is expired</label>
        <input type="checkbox" class="form-check-input" id="inputIsExpired" v-model="product.is_expired">
      </div>
      <div class="mb-3" v-if="product.is_expired == true">
        <label for="inputExpirationDate" class="form-label" >Expiration Date</label>
        <input type="date" class="form-control" id="inputExpirationDate" v-model="product.expiration_date">
      </div>
      <div class="mb-3 form-check">
        <label for="inputIsActive" class="form-label" >Is Visible</label>
        <input type="checkbox" class="form-check-input" id="inputIsActive" v-model="product.is_visible">
      </div>
      <div class="mb-3">
          <label for="inputImage" class="form-label">Image: </label>
          <img v-show="this.$route.params.image" :src="this.$route.params.image" :alt="product.name" class="img-thumbnail">
          <input type="file" class="form-control" id="inputImage" @change="imageUpload" accept="image/jpeg">
      </div>
      <router-link to="/products">
        <button class="btn btn-success me-3"><i class="bi bi-skip-backward-fill"></i></button>
      </router-link>
      <button class="btn btn-primary" @click="editProduct"><i class="bi bi-pencil"></i></button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      product: {
        name: this.$route.params.name,
        description: this.$route.params.description,
        price: this.$route.params.price,
        category: this.$route.params.categoryId,
        unit: this.$route.params.unit,
        quantity: this.$route.params.quantity,
        barcode: this.$route.params.barcode,
        self_price: this.$route.params.self_price,
        is_expired: this.$route.params.is_expired,
        expiration_date: this.$route.params.expiration_date,
        is_available: this.$route.params.is_available,
        is_visible: this.$route.params.is_visible,
      },
      seletedImage: null,
      fd: null,
    }
  },
  methods: {
    
    async editProduct() {
      if (!this.fd) {
        this.fd = this.product
      };
      console.log(this.fd);
      await axios.put(`productedit/${this.$route.params.id}/`, this.fd)
      .then(response => {
        console.log(response);
        if (response.status == 200) {
          alert('Product edited');
          this.$router.push('/products');
        } else {
          alert('Product not edited');
        }
      })
    },
    imageUpload(event) {
      this.selectedImage = event.target.files[0];
      let fd = new FormData();
      fd.append('image', this.selectedImage, this.selectedImage.name);
      fd.append('name', this.product.name);
      fd.append('price', this.product.price);
      fd.append('description', this.product.description);
      fd.append('category', this.product.category); 
      fd.append('unit', this.product.unit);
      fd.append('quantity', this.product.quantity);
      fd.append('barcode', this.product.barcode);
      fd.append('self_price', this.product.self_price);
      fd.append('is_expired', this.product.is_expired);
      fd.append('expiration_date', this.product.expiration_date);
      fd.append('is_available', this.product.is_available);
      fd.append('is_visible', this.product.is_visible);
      this.fd = fd;
      console.log(fd);

    },
  },
  watch: {

  }
  
}

</script>

<style scoped>
  form {
    margin-bottom: 20px;
  }

  img {
    width: 100px;
    height: 100px;
    margin: 10px 10px 10px 10px;
  }
</style>
