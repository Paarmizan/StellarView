<template>
  <button class="btn">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name:"btnSS"

}
</script>

<style lang="scss" scoped>
button{
  width: 497px;
  height: 65px;
  background: #15C6E9;
  border-radius: 19px;
  font-size: 24px;
  position: relative;
  color: white;
  bottom: -350px;
  left: 30px;
  transition: transform 0.3s;


  &:hover {
    transform: scale(1.1);
  }


}

</style>