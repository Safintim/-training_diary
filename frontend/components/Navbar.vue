<template>
  <div>
    <b-navbar toggleable="lg" type="light" variant="light">
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-navbar-nav>
            <b-nav-item href="#">Тренировки</b-nav-item>
            <b-nav-item href="#">Мои тренировки</b-nav-item>
            <b-nav-item href="#">Статистика</b-nav-item>
            <b-nav-item href="#">Блог</b-nav-item>
            <b-nav-item href="#">Прогнозирование</b-nav-item>
          </b-navbar-nav>
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>Аккаунт</em>
            </template>
            <b-dropdown-item href="#">Мой профиль</b-dropdown-item>
            <b-dropdown-item href="#">Выйти</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
