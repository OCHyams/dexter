struct iterator {
  int index_;
  iterator(int index) : index_(index) {}
  bool operator!=(iterator const &rhs) const { return index_ != rhs.index_; }
  int operator*() { return index_; }
  int operator++() { return index_++; }
};

template <int BEGIN, int END> struct range {
  iterator begin() const { return iterator(BEGIN); }
  iterator end() const { return iterator(END); }
};

int sum_range(int argc, char **) {
  range<0, 5> list;
  int total = 0;
  for (volatile auto elem : list)
    total += elem * argc; // DexLabel('check')
  return total;
}

// DexExpectWatchValue('elem', '0', '1', '2', '3', '4', on_line='check')
// DexExpectWatchValue('total', '0', '1', '3', '6', on_line='check')
// DexExpectWatchValue('argc', '1', on_line='check')
