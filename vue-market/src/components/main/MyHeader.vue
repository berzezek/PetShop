<template lang="">
  <!-- Navigation-->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3" id="mainNav">
      <div class="container px-4 px-lg-5">
        <a class="navbar-brand"><router-link to="/">ZooMarket</router-link></a>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ms-auto my-2 my-lg-0">
            <li class="nav-item"><a class="nav-link" ><router-link to="/categories">Categories</router-link></a></li>
            <li class="nav-item"><a class="nav-link" ><router-link to="/products">Products</router-link></a></li>
            <li class="nav-item"><a class="nav-link" ><router-link to="/carts">Basket</router-link></a></li>
          </ul>
        </div>
      </div>
    </nav>
  <router-view></router-view>
</template>
<script>

export default {
  name: 'my-header',
  
}
</script>
<style>

</style>