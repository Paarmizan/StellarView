<template>
  <button class="btn">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name:"butOrder"

}
</script>

<style lang="scss" scoped>
button{
  width: 390px;
  height: 90px;
  background: white;
  border-radius: 19px;
  font-size: 36px;
  top: 40px;
  left: 40px;
  position: absolute;

  transition: 0.3s background-color, transform 0.3s;


  &:hover {
    background-color: #15C6E9;
    transform: scale(1.1);
  }
}
</style>